#!/usr/bin/env python3

import frappe

def update_branding():
    """Update the website settings with Level AI Academy branding"""
    
    # Initialize Frappe
    frappe.init(site='lms.localhost')
    frappe.connect()
    
    try:
        # Get or create Website Settings document
        settings = frappe.get_doc('Website Settings', 'Website Settings')
        
        # Update branding fields
        settings.app_name = 'Level AI Academy'
        settings.title_prefix = 'Level AI Academy'
        
        # Save the document
        settings.save(ignore_permissions=True)
        frappe.db.commit()
        
        print("✅ Successfully updated app name to 'Level AI Academy'")
        
        # Also update LMS Settings if it exists
        try:
            lms_settings = frappe.get_doc('LMS Settings', 'LMS Settings')
            # Any LMS-specific settings can be updated here
            print("✅ LMS Settings document found and ready for updates")
        except frappe.DoesNotExistError:
            print("ℹ️  LMS Settings document not found, will be created when accessed")
            
    except Exception as e:
        print(f"❌ Error updating branding: {str(e)}")
        
    finally:
        frappe.destroy()

if __name__ == '__main__':
    update_branding()