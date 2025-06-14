# Azure OAuth Configuration for Level AI Academy

## Overview
This document provides step-by-step instructions for setting up Google and Microsoft OAuth authentication in Azure for Level AI Academy.

## Prerequisites
- Azure subscription with appropriate permissions
- Google Cloud Platform account
- Microsoft Azure Active Directory access
- Level AI Academy deployed in Azure

## 1. Google OAuth Configuration

### Step 1: Create Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing project
3. Enable the **Google+ API** (required for OAuth)

### Step 2: Create OAuth 2.0 Credentials
1. Navigate to **APIs & Services** → **Credentials**
2. Click **Create Credentials** → **OAuth 2.0 Client ID**
3. Configure the OAuth consent screen first if prompted
4. Select **Web Application** as the application type

### Step 3: Configure OAuth Client
```
Application Name: Level AI Academy
Authorized JavaScript Origins:
  - https://academy.wearelevel.ai
  - https://your-staging-domain.com (for testing)

Authorized Redirect URIs:
  - https://academy.wearelevel.ai/api/method/lms.lms.social_auth.google_callback
  - https://your-staging-domain.com/api/method/lms.lms.social_auth.google_callback
```

### Step 4: Save Credentials
- Copy the **Client ID** and **Client Secret**
- Store these securely in Azure Key Vault

## 2. Microsoft OAuth Configuration

### Step 1: Register Application in Azure AD
1. Go to [Azure Portal](https://portal.azure.com/)
2. Navigate to **Azure Active Directory** → **App registrations**
3. Click **New registration**

### Step 2: Configure App Registration
```
Name: Level AI Academy
Supported account types: Accounts in any organizational directory and personal Microsoft accounts
Redirect URI (Web): https://academy.wearelevel.ai/api/method/lms.lms.social_auth.microsoft_callback
```

### Step 3: Create Client Secret
1. Go to **Certificates & secrets**
2. Click **New client secret**
3. Add description: "Level AI Academy OAuth"
4. Set expiration (24 months recommended)
5. Copy the secret value immediately (it won't be shown again)

### Step 4: Configure API Permissions
1. Go to **API permissions**
2. Click **Add a permission** → **Microsoft Graph**
3. Select **Delegated permissions**
4. Add these permissions:
   - `openid` - Sign in and read user profile
   - `email` - View users' email address  
   - `profile` - View users' basic profile
5. Click **Add permissions**
6. Click **Grant admin consent** (if you have admin rights)

### Step 5: Save Configuration
- Copy the **Application (client) ID**
- Copy the **Client Secret** from step 3
- Store these securely in Azure Key Vault

## 3. Azure Key Vault Setup

### Create Key Vault
```bash
# Create Key Vault
az keyvault create \
  --resource-group level-ai-academy-rg \
  --name level-academy-secrets \
  --location uksouth \
  --sku standard

# Set secrets
az keyvault secret set \
  --vault-name level-academy-secrets \
  --name google-client-id \
  --value "your-google-client-id"

az keyvault secret set \
  --vault-name level-academy-secrets \
  --name google-client-secret \
  --value "your-google-client-secret"

az keyvault secret set \
  --vault-name level-academy-secrets \
  --name microsoft-client-id \
  --value "your-microsoft-client-id"

az keyvault secret set \
  --vault-name level-academy-secrets \
  --name microsoft-client-secret \
  --value "your-microsoft-client-secret"
```

### Configure App Service Access
```bash
# Enable managed identity for App Service
az webapp identity assign \
  --resource-group level-ai-academy-rg \
  --name level-academy-app

# Grant Key Vault access to App Service
az keyvault set-policy \
  --name level-academy-secrets \
  --object-id <app-service-principal-id> \
  --secret-permissions get list
```

## 4. Application Configuration

### Environment Variables for App Service
```bash
# Add these app settings to your Azure App Service
GOOGLE_CLIENT_ID=@Microsoft.KeyVault(VaultName=level-academy-secrets;SecretName=google-client-id)
GOOGLE_CLIENT_SECRET=@Microsoft.KeyVault(VaultName=level-academy-secrets;SecretName=google-client-secret)
MICROSOFT_CLIENT_ID=@Microsoft.KeyVault(VaultName=level-academy-secrets;SecretName=microsoft-client-id)
MICROSOFT_CLIENT_SECRET=@Microsoft.KeyVault(VaultName=level-academy-secrets;SecretName=microsoft-client-secret)
```

### LMS Settings Configuration
1. Login to your Frappe site as administrator
2. Go to **LMS Settings**
3. Navigate to **Signup Settings** tab
4. In the **Social Login** section:
   - Check **Enable Google Login**
   - Enter your Google Client ID
   - Enter your Google Client Secret
   - Check **Enable Microsoft Login**  
   - Enter your Microsoft Client ID
   - Enter your Microsoft Client Secret
5. Save the settings

## 5. Testing OAuth Flow

### Test URLs
```
Google OAuth Test:
https://academy.wearelevel.ai/api/method/lms.lms.social_auth.initiate_oauth?provider=google

Microsoft OAuth Test:
https://academy.wearelevel.ai/api/method/lms.lms.social_auth.initiate_oauth?provider=microsoft
```

### Verification Steps
1. Navigate to the login page: `https://academy.wearelevel.ai/login`
2. Click "Continue with Google" or "Continue with Microsoft"
3. Complete OAuth flow with your account
4. Verify user is created in Frappe with correct details
5. Check that social login IDs are stored in user profile

## 6. Security Considerations

### Production Checklist
- [ ] Use HTTPS for all redirect URIs
- [ ] Store secrets in Azure Key Vault, not environment variables
- [ ] Regularly rotate OAuth client secrets
- [ ] Monitor OAuth application usage in provider consoles
- [ ] Implement rate limiting on OAuth endpoints
- [ ] Add proper error handling and logging
- [ ] Test with various user types (organization vs individual)

### OAuth Consent Screen
- Configure OAuth consent screen with your organization branding
- Add privacy policy and terms of service URLs
- Request only necessary scopes (openid, email, profile)
- Consider verification for production use

## 7. Troubleshooting

### Common Issues
1. **Redirect URI Mismatch**: Ensure exact match including protocol (https)
2. **Invalid Client**: Check client ID and secret are correct
3. **Scope Errors**: Verify requested permissions are granted
4. **CORS Issues**: Ensure domain is added to authorized origins
5. **Key Vault Access**: Verify App Service managed identity has access

### Debug Mode
Add this to your Frappe site config for detailed OAuth logging:
```python
# site_config.json
{
  "developer_mode": 1,
  "log_level": "DEBUG"
}
```

## 8. Organization Integration

### Automatic Organization Assignment
The social auth system can automatically assign users to organizations based on:
- Email domain matching
- Pre-configured organization mappings
- Admin approval workflows

### Admin Configuration
Organization administrators can:
- Enable/disable social login for their organization
- View social login usage analytics
- Manage user permissions and roles

This setup provides a seamless OAuth experience for users while maintaining security and compliance with organizational requirements.