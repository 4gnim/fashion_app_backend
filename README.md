# E-Commerce Fashion Backend API

## Description

This is a backend API program that supports a Flutter-based e-commerce fashion application. The backend provides various features to support the app's operations, including authentication, product management, user management, and transaction features.

## Technologies Used

- **Backend Framework**: Django
- **Database**: SQLite (Django default)
- **Authentication**: Django Authentication
- **API Format**: RESTful (with Django REST Framework)

## Key Features

1. **User Authentication**:
   - User registration and login.
   - Session management.
2. **Product Management**:
   - Add, edit, and delete products.
   - Product listing with search and filters.
3. **User Management**:
   - User profile.
   - Purchase history.
4. **Transactions**:
   - Order processing.
   - Order status management.
5. **Application Pages**:
   - **Home**: Displays featured products and categories.
   - **Wishlist**: Saves users' favorite products.
   - **Cart**: Manages products to be purchased.
   - **Profile**: Displays and updates user information.
6. **Integration with Flutter**:
   - This API is designed to work seamlessly with the Flutter application.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/4gnim/fashion-app-backend.git
   ```
2. Navigate to the project directory:
   ```bash
   cd repo-name
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # for Linux/Mac
   env\Scripts\activate   # for Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the Django project:
   ```bash
   django-admin startproject backend .
   ```
6. Run database migrations:
   ```bash
   python manage.py migrate
   ```
7. Start the server:
   ```bash
   python manage.py runserver
   ```

## License

This project is licensed under the [MIT License](LICENSE).
