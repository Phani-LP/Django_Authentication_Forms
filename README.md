# Django Authentication Forms

This is a Django-based web application that demonstrates user authentication functionality, including user registration, login, logout, and a protected dashboard page.

## Features

- **User Registration**: Users can register with a username, email, and password.
- **User Login**: Registered users can log in using their credentials.
- **User Logout**: Users can log out of their accounts.
- **Dashboard**: A protected page accessible only to logged-in users.
- **CSRF Protection**: Secure forms with CSRF tokens.

## Project Structure

AuthenticationForm/ __init__.py asgi.py settings.py urls.py wsgi.py Users/ __init__.py admin.py apps.py forms.py models.py tests.py urls.py views.py migrations/ templates/ Users/ login.html register.html dashboard.html index.html db.sqlite3 manage.py README.md


## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Django_Authentication_Forms

2. Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the required dependencies:
pip install -r requirements.txt

4. Apply migrations:
python manage.py migrate

5. Run the development server:
python manage.py runserver

6. Open the application in your browser at http://127.0.0.1:8000/.

# Usage
<ul>
<li>Visit the home page to navigate to the login or registration page.</li>
<li>Register a new user account.</li>
<li>Log in with the registered credentials.</li>
<li>Access the dashboard after logging in.</li>
<li>Log out to return to the login page.</li>
</ul>

# File Descriptions
<ul>
<li><strong>AuthenticationForm/settings.py: </strong>Contains project settings, including database configuration and installed apps.</li>
<li><strong>AuthenticationForm/urls.py: </strong>Defines the URL routing for the project.</li>
<li><strong>Users/forms.py: </strong>Contains custom forms for user registration and login.</li>
<li><strong>Users/views.py: </strong>Implements the logic for user registration, login, logout, and dashboard.</li>
<li><strong>Users/templates/Users/: </strong>Contains HTML templates for the application.</li>
<li><strong>db.sqlite3: </strong>SQLite database file.</li></ul>
