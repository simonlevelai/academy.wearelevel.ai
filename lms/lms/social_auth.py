"""
Social Authentication for Level AI Academy
Handles Google and Microsoft OAuth login flows
"""

import frappe
import requests
import json
from urllib.parse import urlencode
from frappe.utils import get_url
from frappe.auth import LoginManager


@frappe.whitelist(allow_guest=True)
def get_oauth_config(provider):
    """Get OAuth configuration for a provider"""
    settings = frappe.get_single("LMS Settings")
    
    if provider == "google" and settings.enable_google_login:
        return {
            "enabled": True,
            "client_id": settings.google_client_id,
            "auth_url": "https://accounts.google.com/o/oauth2/v2/auth",
            "scope": "openid email profile",
            "redirect_uri": get_url("/api/method/lms.lms.social_auth.google_callback")
        }
    elif provider == "microsoft" and settings.enable_microsoft_login:
        return {
            "enabled": True,
            "client_id": settings.microsoft_client_id,
            "auth_url": "https://login.microsoftonline.com/common/oauth2/v2.0/authorize",
            "scope": "openid email profile",
            "redirect_uri": get_url("/api/method/lms.lms.social_auth.microsoft_callback")
        }
    
    return {"enabled": False}


@frappe.whitelist(allow_guest=True)
def initiate_oauth(provider):
    """Initiate OAuth flow by redirecting to provider"""
    config = get_oauth_config(provider)
    
    if not config["enabled"]:
        frappe.throw(f"{provider.title()} login is not enabled")
    
    # Generate state parameter for security
    state = frappe.generate_hash(length=32)
    frappe.cache().set_value(f"oauth_state_{state}", provider, expires_in_sec=600)
    
    params = {
        "client_id": config["client_id"],
        "redirect_uri": config["redirect_uri"],
        "response_type": "code",
        "scope": config["scope"],
        "state": state
    }
    
    auth_url = f"{config['auth_url']}?{urlencode(params)}"
    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = auth_url


@frappe.whitelist(allow_guest=True)
def google_callback():
    """Handle Google OAuth callback"""
    return handle_oauth_callback("google")


@frappe.whitelist(allow_guest=True)
def microsoft_callback():
    """Handle Microsoft OAuth callback"""
    return handle_oauth_callback("microsoft")


def handle_oauth_callback(provider):
    """Generic OAuth callback handler"""
    code = frappe.form_dict.get("code")
    state = frappe.form_dict.get("state")
    error = frappe.form_dict.get("error")
    
    if error:
        frappe.throw(f"OAuth error: {error}")
    
    if not code or not state:
        frappe.throw("Invalid OAuth response")
    
    # Verify state parameter
    cached_provider = frappe.cache().get_value(f"oauth_state_{state}")
    if cached_provider != provider:
        frappe.throw("Invalid OAuth state")
    
    # Clear the state
    frappe.cache().delete_key(f"oauth_state_{state}")
    
    # Exchange code for access token
    token_data = exchange_code_for_token(provider, code)
    
    # Get user profile
    user_info = get_user_profile(provider, token_data["access_token"])
    
    # Create or login user
    user = create_or_login_user(user_info, provider)
    
    # Login the user
    login_manager = LoginManager()
    login_manager.login_as(user)
    
    # Redirect to dashboard
    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = "/lms"


def exchange_code_for_token(provider, code):
    """Exchange authorization code for access token"""
    settings = frappe.get_single("LMS Settings")
    
    if provider == "google":
        token_url = "https://oauth2.googleapis.com/token"
        client_id = settings.google_client_id
        client_secret = settings.google_client_secret
        redirect_uri = get_url("/api/method/lms.lms.social_auth.google_callback")
    elif provider == "microsoft":
        token_url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
        client_id = settings.microsoft_client_id
        client_secret = settings.microsoft_client_secret
        redirect_uri = get_url("/api/method/lms.lms.social_auth.microsoft_callback")
    else:
        frappe.throw(f"Unsupported provider: {provider}")
    
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": redirect_uri
    }
    
    response = requests.post(token_url, data=data)
    if response.status_code != 200:
        frappe.throw(f"Failed to exchange code for token: {response.text}")
    
    return response.json()


def get_user_profile(provider, access_token):
    """Get user profile from OAuth provider"""
    headers = {"Authorization": f"Bearer {access_token}"}
    
    if provider == "google":
        profile_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    elif provider == "microsoft":
        profile_url = "https://graph.microsoft.com/v1.0/me"
    else:
        frappe.throw(f"Unsupported provider: {provider}")
    
    response = requests.get(profile_url, headers=headers)
    if response.status_code != 200:
        frappe.throw(f"Failed to get user profile: {response.text}")
    
    profile_data = response.json()
    
    # Normalize user data across providers
    if provider == "google":
        return {
            "email": profile_data.get("email"),
            "first_name": profile_data.get("given_name", ""),
            "last_name": profile_data.get("family_name", ""),
            "full_name": profile_data.get("name", ""),
            "picture": profile_data.get("picture"),
            "provider": "google",
            "provider_id": profile_data.get("id")
        }
    elif provider == "microsoft":
        return {
            "email": profile_data.get("mail") or profile_data.get("userPrincipalName"),
            "first_name": profile_data.get("givenName", ""),
            "last_name": profile_data.get("surname", ""),
            "full_name": profile_data.get("displayName", ""),
            "picture": None,  # Microsoft Graph requires additional API call
            "provider": "microsoft",
            "provider_id": profile_data.get("id")
        }


def create_or_login_user(user_info, provider):
    """Create new user or return existing user"""
    email = user_info["email"]
    
    if not email:
        frappe.throw("Email not provided by OAuth provider")
    
    # Check if user already exists
    if frappe.db.exists("User", email):
        user = frappe.get_doc("User", email)
        
        # Update social login info if not already set
        if not user.get(f"{provider}_id"):
            user.set(f"{provider}_id", user_info["provider_id"])
            user.save(ignore_permissions=True)
        
        return user.name
    
    # Create new user
    user = frappe.get_doc({
        "doctype": "User",
        "email": email,
        "first_name": user_info["first_name"] or email.split("@")[0],
        "last_name": user_info["last_name"] or "",
        "full_name": user_info["full_name"] or user_info["first_name"] or email.split("@")[0],
        "username": email,
        "user_type": "Website User",
        "send_welcome_email": 0,
        "enabled": 1
    })
    
    # Add social login identifier
    user.set(f"{provider}_id", user_info["provider_id"])
    
    # Add default role
    user.append("roles", {"role": "LMS Student"})
    
    # Set profile picture if available
    if user_info.get("picture"):
        try:
            # Download and attach profile picture
            import requests
            img_response = requests.get(user_info["picture"])
            if img_response.status_code == 200:
                file_doc = frappe.get_doc({
                    "doctype": "File",
                    "file_name": f"profile_{email.replace('@', '_')}.jpg",
                    "content": img_response.content,
                    "attached_to_doctype": "User",
                    "attached_to_name": email,
                    "is_private": 0
                })
                file_doc.insert(ignore_permissions=True)
                user.user_image = file_doc.file_url
        except Exception:
            # Profile picture upload failed, continue without it
            pass
    
    user.insert(ignore_permissions=True)
    
    return user.name


@frappe.whitelist(allow_guest=True)
def get_social_login_buttons():
    """Get configuration for social login buttons on frontend"""
    settings = frappe.get_single("LMS Settings")
    
    buttons = []
    
    if settings.enable_google_login and settings.google_client_id:
        buttons.append({
            "provider": "google",
            "name": "Google",
            "icon": "google",
            "color": "#4285f4",
            "url": "/api/method/lms.lms.social_auth.initiate_oauth?provider=google"
        })
    
    if settings.enable_microsoft_login and settings.microsoft_client_id:
        buttons.append({
            "provider": "microsoft", 
            "name": "Microsoft",
            "icon": "microsoft",
            "color": "#00a4ef",
            "url": "/api/method/lms.lms.social_auth.initiate_oauth?provider=microsoft"
        })
    
    return buttons