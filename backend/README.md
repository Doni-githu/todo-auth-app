# Todo App Backend

## Overview
This is the backend for a Todo application. It is built using Django, a high-level Python web framework. The backend provides APIs for managing users, projects, and tasks (todos).

## Features
- User authentication and management
- Project creation and management
- Task (Todo) creation, assignment, and tracking
- Token-based authentication

## Project Structure
- `config/`: Contains the main configuration files for the Django project.
- `projects/`: Handles project-related functionality, including models, views, serializers, and URLs.
- `user/`: Manages user-related functionality, including authentication, models, views, and serializers.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django's command-line utility for administrative tasks.

## Installation

### Prerequisites
- Python 3.12 or higher
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd backend
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- `POST /api/token/`: Obtain a token for authentication.
- `POST /api/token/refresh/`: Refresh the authentication token.

### Projects
- `GET /projects/`: List all projects.
- `POST /projects/`: Create a new project.

### Todos
- `GET /todos/`: List all tasks.
- `POST /todos/`: Create a new task.

## Contributing
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your branch.
4. Submit a pull request.

## License
This project is licensed under the MIT License.