# Project: Level AI Academy

## Project Overview
Level AI Academy is a fork of Frappe LMS customized for Level AI's educational platform. This learning management system will provide AI-focused courses and training materials.

## Tech Stack
- **Framework**: Frappe Framework (Python backend, Vue.js frontend)
- **Database**: MariaDB 10.8
- **Cache**: Redis
- **Development**: Docker-based development environment

## Development Setup

### Prerequisites
- Docker and Docker Compose installed
- Git

### Running the Application
1. Start Docker containers: `docker compose up -d`
2. Access the application at: http://localhost:8000/lms
3. Login credentials:
   - Username: Administrator
   - Password: admin

### Stopping the Application
- Stop containers: `docker compose down`
- Stop and remove volumes: `docker compose down -v`

## Project Structure
- `/frontend/` - Vue.js frontend application
- `/lms/` - Main LMS Python module
- `/docker/` - Docker configuration files
- `docker-compose.yml` - Docker compose configuration
- `init.sh` - Initialization script for Frappe bench

## Key Customization Areas for Level AI Academy

### 1. Branding (See brandguidelines.md for full details)
- **Logo**: Update in `/frontend/public/` and `/lms/public/images/`
- **Colors**: Implement brand colors in `/frontend/tailwind.config.js`
  - Primary Blue: #2563EB
  - Deep Purple: #7C3AED
  - Teal Accent: #14B8A6
  - Orange Accent: #F59E0B
- **Typography**: Inter font family (already included)
- **Site Title**: "Level AI Academy" in LMS Settings

### 2. Course Categories (Per Brand Guidelines)
- Fundamentals of AI
- Machine Learning
- Deep Learning
- Natural Language Processing
- Computer Vision
- AI Ethics & Responsibility
- Practical AI Applications
- AI for Business

### 3. Frontend Customization
- Main app entry: `/frontend/src/App.vue`
- Course components: `/frontend/src/components/`
- Pages: `/frontend/src/pages/`

### 4. Backend Customization
- API endpoints: `/lms/lms/api.py`
- DocTypes (data models): `/lms/lms/doctype/`
- Custom business logic in respective Python files

## Development Guidelines
- Follow Frappe Framework conventions
- Use the bench command for Frappe-specific operations
- Frontend changes require rebuilding: `docker compose exec frappe bench build --app lms`
- Clear cache after backend changes: `docker compose exec frappe bench --site lms.localhost clear-cache`

## Testing Commands
- Run Python tests: `docker compose exec frappe bench --site lms.localhost run-tests --app lms`
- Access Frappe console: `docker compose exec frappe bench --site lms.localhost console`

## Common Tasks
- Create new DocType: Use Frappe UI or `bench new-doctype`
- Add new page: Create Vue component in `/frontend/src/pages/` and add route
- Modify email templates: Edit files in `/lms/templates/emails/`

## Deployment Notes
- For production, use Frappe Cloud or self-host with proper WSGI server
- Environment variables for production should be set appropriately
- SSL certificates required for production deployment