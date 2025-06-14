#!/usr/bin/env python3

import frappe

def create_level_ai_categories():
    """Create Level.ai focused course categories"""
    
    # Initialize Frappe
    frappe.init(site='lms.localhost')
    frappe.connect()
    
    categories = [
        {
            'name': 'AI for Social Impact',
            'description': 'Using AI to maximize community benefit and social change'
        },
        {
            'name': 'Charity & Non-Profit AI Tools',
            'description': 'Practical AI applications for purpose-driven organizations'
        },
        {
            'name': 'Ethical AI Implementation',
            'description': 'Responsible AI practices for social enterprises'
        },
        {
            'name': 'AI for Resource Optimization',
            'description': 'Helping charities do more with less through automation'
        },
        {
            'name': 'Data for Good',
            'description': 'Using data science to measure and increase social impact'
        },
        {
            'name': 'AI Leadership for Non-Profits',
            'description': 'Strategic AI guidance for charity directors and leaders'
        },
        {
            'name': 'Grant Writing with AI',
            'description': 'Using AI to improve funding applications and proposals'
        },
        {
            'name': 'Impact Measurement with AI',
            'description': 'Data-driven approaches to measuring social outcomes'
        }
    ]
    
    try:
        for cat in categories:
            try:
                # Check if category already exists
                if frappe.db.exists('LMS Category', {'title': cat['name']}):
                    print(f"Category '{cat['name']}' already exists, skipping...")
                    continue
                    
                doc = frappe.new_doc('LMS Category')
                doc.title = cat['name']
                doc.description = cat['description']
                doc.published = 1
                doc.insert(ignore_permissions=True)
                print(f"✅ Created category: {cat['name']}")
            except Exception as e:
                print(f"❌ Error creating {cat['name']}: {str(e)}")
        
        frappe.db.commit()
        print("✅ Successfully created Level.ai course categories!")
        
    except Exception as e:
        print(f"❌ Error creating categories: {str(e)}")
        
    finally:
        frappe.destroy()

if __name__ == '__main__':
    create_level_ai_categories()