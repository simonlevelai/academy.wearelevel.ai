import frappe
from frappe.model.document import Document

class LMSOrganization(Document):
    def validate(self):
        self.validate_email()
        self.validate_team_size()
    
    def validate_email(self):
        """Validate primary contact email format"""
        if self.primary_contact_email:
            frappe.utils.validate_email_address(self.primary_contact_email, True)
    
    def validate_team_size(self):
        """Ensure max_learners is reasonable for team size"""
        if self.max_learners and self.max_learners < 1:
            frappe.throw("Maximum learners must be at least 1")
        
        # Set reasonable defaults based on team size
        if not self.max_learners:
            size_mapping = {
                "1-5": 5,
                "6-20": 20, 
                "21-50": 50,
                "51-100": 100,
                "100+": 200
            }
            self.max_learners = size_mapping.get(self.team_size, 10)
    
    def after_insert(self):
        """Create organization admin user if needed"""
        self.create_admin_user()
        self.send_welcome_email()
    
    def create_admin_user(self):
        """Create user account for organization administrator"""
        if not self.admin_user and self.primary_contact_email:
            # Check if user already exists
            if frappe.db.exists("User", self.primary_contact_email):
                self.admin_user = self.primary_contact_email
                self.save()
                return
            
            # Create new user
            user = frappe.get_doc({
                "doctype": "User",
                "email": self.primary_contact_email,
                "first_name": self.primary_contact_name.split(" ")[0],
                "last_name": " ".join(self.primary_contact_name.split(" ")[1:]) if " " in self.primary_contact_name else "",
                "username": self.primary_contact_email,
                "user_type": "Website User",
                "send_welcome_email": 0,
                "organization": self.name
            })
            
            # Add organization admin role
            user.append("roles", {
                "role": "LMS Organization Admin"
            })
            
            user.insert(ignore_permissions=True)
            
            # Update organization record
            self.admin_user = user.name
            self.save()
    
    def send_welcome_email(self):
        """Send welcome email to organization admin"""
        if self.primary_contact_email:
            # This would send a custom welcome email template
            # For now, just log it
            frappe.logger().info(f"Welcome email would be sent to {self.primary_contact_email} for organization {self.name}")
    
    def get_team_members(self):
        """Get all team members for this organization"""
        return frappe.get_all("User", 
            filters={"organization": self.name, "enabled": 1},
            fields=["name", "full_name", "email", "creation"]
        )
    
    def add_team_member(self, email, full_name):
        """Add a new team member to the organization"""
        if len(self.get_team_members()) >= self.max_learners:
            frappe.throw(f"Maximum learner limit of {self.max_learners} reached")
        
        # Check if user exists
        if frappe.db.exists("User", email):
            user = frappe.get_doc("User", email)
            user.organization = self.name
            user.save()
        else:
            # Create new user
            user = frappe.get_doc({
                "doctype": "User",
                "email": email,
                "first_name": full_name.split(" ")[0],
                "last_name": " ".join(full_name.split(" ")[1:]) if " " in full_name else "",
                "username": email,
                "user_type": "Website User",
                "organization": self.name,
                "send_welcome_email": 1
            })
            
            # Add LMS Student role
            user.append("roles", {
                "role": "LMS Student"
            })
            
            user.insert(ignore_permissions=True)
        
        return user.name


# API endpoints for Organization Registration and Team Management

@frappe.whitelist(allow_guest=True)
def register_organization(data):
    """Create a new organization registration"""
    try:
        org_data = frappe.parse_json(data)
        
        # Create LMS Organization record
        org = frappe.get_doc({
            "doctype": "LMS Organization",
            "organization_name": org_data.get("organizationName"),
            "organization_type": org_data.get("organizationType"),
            "organization_description": org_data.get("description"),
            "website": org_data.get("website"),
            "charity_registration_number": org_data.get("registrationNumber"),
            "sector": org_data.get("sector"),
            "primary_contact_name": org_data.get("contactName"),
            "primary_contact_email": org_data.get("contactEmail"),
            "phone_number": org_data.get("phoneNumber"),
            "country": org_data.get("country"),
            "address": org_data.get("address"),
            "team_size": org_data.get("teamSize"),
            "max_learners": org_data.get("maxLearners", 10),
            "enable_team_reporting": org_data.get("enableReporting", True),
            "custom_branding": org_data.get("customBranding", False),
            "ai_focus_areas": org_data.get("aiFocusAreas", ""),
            "learning_goals": org_data.get("learningGoals", ""),
            "status": "Active"
        })
        
        org.insert(ignore_permissions=True)
        
        return {
            "success": True,
            "organization_id": org.name,
            "message": "Organization registered successfully"
        }
        
    except Exception as e:
        frappe.log_error(f"Organization registration failed: {str(e)}")
        return {
            "success": False,
            "message": f"Registration failed: {str(e)}"
        }


@frappe.whitelist()
def get_organization_team_stats(organization):
    """Get team statistics for an organization"""
    try:
        org = frappe.get_doc("LMS Organization", organization)
        team_members = org.get_team_members()
        
        # Calculate stats
        total_members = len(team_members)
        active_learners = len([m for m in team_members if m.get('last_active')])
        
        # Get course completion stats
        courses_completed = frappe.db.count("LMS Certificate", {
            "member": ["in", [m.name for m in team_members]],
            "published": 1
        })
        
        # Calculate average progress
        enrollments = frappe.get_all("LMS Enrollment", 
            filters={"member": ["in", [m.name for m in team_members]]},
            fields=["progress"]
        )
        
        if enrollments:
            total_progress = sum([float(e.progress.replace('%', '')) if e.progress else 0 for e in enrollments])
            avg_progress = round(total_progress / len(enrollments))
        else:
            avg_progress = 0
        
        return {
            "totalMembers": total_members,
            "activeLearners": active_learners,
            "coursesCompleted": courses_completed,
            "avgProgress": avg_progress
        }
        
    except Exception as e:
        frappe.log_error(f"Failed to get team stats: {str(e)}")
        return {"error": str(e)}


@frappe.whitelist()
def get_organization_team_members(organization):
    """Get detailed team member information"""
    try:
        org = frappe.get_doc("LMS Organization", organization)
        team_members = []
        
        # Get all team members
        users = frappe.get_all("User", 
            filters={"organization": organization, "enabled": 1},
            fields=["name", "full_name", "email", "creation", "last_active"]
        )
        
        for user in users:
            # Get enrollments and progress
            enrollments = frappe.get_all("LMS Enrollment",
                filters={"member": user.name},
                fields=["course", "progress"]
            )
            
            # Get user role
            roles = frappe.get_roles(user.name)
            if "LMS Organization Admin" in roles:
                role = "Admin"
            else:
                role = "Member"
            
            # Calculate average progress
            if enrollments:
                total_progress = sum([float(e.progress.replace('%', '')) if e.progress else 0 for e in enrollments])
                avg_progress = round(total_progress / len(enrollments))
            else:
                avg_progress = 0
            
            # Get recent activity
            recent_activity = []
            recent_progress = frappe.get_all("LMS Course Progress",
                filters={"member": user.name},
                fields=["creation", "lesson"],
                order_by="creation desc",
                limit=3
            )
            
            for activity in recent_progress:
                lesson_title = frappe.db.get_value("Course Lesson", activity.lesson, "title")
                recent_activity.append({
                    "id": len(recent_activity) + 1,
                    "action": f"Completed \"{lesson_title}\"",
                    "date": activity.creation.strftime("%Y-%m-%d")
                })
            
            # Get course details
            courses = []
            for enrollment in enrollments:
                course_title = frappe.db.get_value("LMS Course", enrollment.course, "title")
                progress = float(enrollment.progress.replace('%', '')) if enrollment.progress else 0
                courses.append({
                    "name": course_title,
                    "progress": progress
                })
            
            team_members.append({
                "id": user.name,
                "name": user.full_name or user.name,
                "email": user.email,
                "role": role,
                "coursesEnrolled": len(enrollments),
                "progress": avg_progress,
                "lastActive": user.last_active.strftime("%Y-%m-%d") if user.last_active else user.creation.strftime("%Y-%m-%d"),
                "courses": courses,
                "recentActivity": recent_activity
            })
        
        return team_members
        
    except Exception as e:
        frappe.log_error(f"Failed to get team members: {str(e)}")
        return {"error": str(e)}


@frappe.whitelist()
def invite_team_member(organization, name, email, role="Member", message=""):
    """Invite a new team member to the organization"""
    try:
        org = frappe.get_doc("LMS Organization", organization)
        
        # Check if user has permission (is organization admin)
        user_roles = frappe.get_roles(frappe.session.user)
        if "LMS Organization Admin" not in user_roles and "System Manager" not in user_roles:
            return {"success": False, "message": "Permission denied"}
        
        # Add team member
        user_id = org.add_team_member(email, name)
        
        # Add admin role if specified
        if role == "Admin":
            user = frappe.get_doc("User", user_id)
            user.append("roles", {"role": "LMS Organization Admin"})
            user.save()
        
        return {
            "success": True,
            "message": f"Successfully invited {name} to the team",
            "user_id": user_id
        }
        
    except Exception as e:
        frappe.log_error(f"Failed to invite team member: {str(e)}")
        return {"success": False, "message": str(e)}


@frappe.whitelist()
def remove_team_member(organization, user_id):
    """Remove a team member from the organization"""
    try:
        # Check if user has permission (is organization admin)
        user_roles = frappe.get_roles(frappe.session.user)
        if "LMS Organization Admin" not in user_roles and "System Manager" not in user_roles:
            return {"success": False, "message": "Permission denied"}
        
        # Remove organization association
        frappe.db.set_value("User", user_id, "organization", "")
        
        return {
            "success": True,
            "message": "Team member removed successfully"
        }
        
    except Exception as e:
        frappe.log_error(f"Failed to remove team member: {str(e)}")
        return {"success": False, "message": str(e)}