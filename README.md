# Project Search Engine

This project is a web application developed using Django, REST framework, HTML, and CSS. It provides functionalities for user authentication (signup, login), employee data management (upload, store, retrieve, edit), and more.

## Features

- **User Authentication**
  - Signup: New users can create accounts to access the system.
  - Login: Registered users can log in securely.
- **Employee Management**
  - Upload: Upload employee details including name, position, contact information, etc.
  - Store: Store employee data securely in the database.
  - Retrieve: Fetch employee details based on search queries or specific criteria.
  - Edit: Update or modify employee information as needed.
- **REST API**
  - Provides a RESTful API for interacting with employee data programmatically.
- **Responsive Design**
  - User-friendly interface designed using HTML and CSS for seamless navigation.

## Technologies Used

- Django: Backend framework for handling server-side logic and database operations.
- Django REST framework: Used for creating RESTful APIs for employee management.
- HTML & CSS: Frontend technologies for designing and styling web pages.
- SQLite (or your preferred database): Database for storing employee information.

## Setup Instructions

1. Clone the repository to your local machine.
2. Install Python and Django if not already installed.
3. Create a virtual environment and activate it.
4. Install required dependencies using `pip install -r requirements.txt`.
5. Run database migrations using `python manage.py migrate`.
6. Create a superuser using `python manage.py createsuperuser` to access the admin panel.
7. Start the development server with `python manage.py runserver`.

## Usage

1. Access the application through the browser at `http://localhost:8000/`.
2. Sign up or log in to access the employee management features.
3. Upload, store, retrieve, and edit employee details as needed.
4. Explore the REST API endpoints for programmatic access to data.
