# Quiz 4 Unified Repository

This repository contains both the Django backend and the frontend template.

- Backend: backend/
- Frontend: frontend-template/

## Tech Stack

- Backend: Django, Django REST Framework, SimpleJWT
- Frontend: React (template)

## Backend Setup

1. Create and activate a virtual environment

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run migrations

```
cd backend
python manage.py makemigrations
python manage.py migrate
```

4. Create an admin user

```
python manage.py createsuperuser
```

5. Run the server

```
python manage.py runserver
```

The backend runs at http://127.0.0.1:8000/

## Frontend Setup

```
cd frontend-template
npm install
npm start
```

The frontend runs at http://localhost:3000/

## Roles and Statuses

Role values for users:

- ADMIN
- MANAGER
- USER

Status values for projects and tasks:

- CREATED
- IN PROGRESS
- OVERDUE
- COMPLETED

## Authentication (SimpleJWT)

Obtain an access token:

- POST /api/auth/token/

```
{
  "username": "admin",
  "password": "adminpassword"
}
```

Refresh token:

- POST /api/auth/token/refresh/

```
{
  "refresh": "<refresh_token>"
}
```

Use the access token as a Bearer token in Postman:

- Authorization -> Bearer Token -> <access_token>

## API Endpoints and Postman Steps

### 1) Create User (Admin only)

- POST /api/users/

Body:

```
{
  "first_name": "Jane",
  "last_name": "Doe",
  "username": "janedoe",
  "email": "jane@example.com",
  "role": "MANAGER",
  "password": "StrongPass123"
}
```

### 2) Create Project (Admin only)

- POST /api/projects/create/

Body:

```
{
  "project_name": "Project Alpha",
  "project_description": "Project Alpha description",
  "start_date": "2026-02-06",
  "end_date": "2026-02-10"
}
```

Behavior:

- If start_date equals today, status is IN PROGRESS
- Otherwise status is CREATED

### 3) List Projects

- GET /api/projects/

Behavior:

- Admin sees all projects
- Manager and User see only projects linked to tasks assigned to them

### 4) Project Detail

- GET /api/projects/<id>/

Behavior:

- Admin sees any project
- Manager and User see only projects linked to tasks assigned to them

### 5) Create Task (Admin or Manager)

- POST /api/tasks/create/

Body:

```
{
  "project": 1,
  "task_name": "Set up database",
  "task_description": "Create models and migrations",
  "user_assigned": 2,
  "start_date": "2026-02-06",
  "end_date": "2026-02-07"
}
```

Behavior:

- If start_date equals today, status is IN PROGRESS
- Otherwise status is CREATED

### 6) Update Task Status (Assigned user, Admin, or Manager)

- PATCH /api/tasks/<id>/

Body:

```
{
  "status": "COMPLETED"
}
```

Behavior:

- When status is updated to COMPLETED, task hours_consumed is calculated using:
  - completion_date (the date the status was set to COMPLETED)
  - start_date
- Example: start_date 2026-01-01, completed on 2026-01-03 -> 48 hours
- Project hours_consumed is automatically recalculated as the sum of all task hours

## Notes on Signals

- Task hours are calculated when a task status transitions to COMPLETED.
- Project hours are recalculated whenever a task is saved or deleted.

## Repository Management Note

If the frontend work is completed by another student, commit it once in this repository. The commit message for that single frontend commit should include all original frontend commit messages from the other student.
