# Human Resources

**Human Resources** is a web application based on the MTV (Model-Template-View) architecture, developed in Django. The application allows storing and viewing employee data.

## Contents

- [Running the Server](#running-the-server)
- [Application Structure](#application-structure)
- [Features](#features)
- [Technologies](#technologies)

---

## Running the Server

To run the project locally, follow these steps:

1. **Clone the Repository**:

    If downloading the project from GitHub, clone the repository using `git clone`:

    ```bash
    git clone https://github.com/anasicic/human_resources.git
    ```

2. **Navigate to the Project Directory**:

    After cloning the project, navigate to the project directory:

    ```bash
    cd human_resources
    ```

3. **Install Required Packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create Migration Files for the Database**:

    ```bash
    python manage.py makemigrations
    ```

5. **Apply Migrations to Implement Changes in the Database**:

    ```bash
    python manage.py migrate
    ```

6. **Run the Development Server**:

    ```bash
    python manage.py runserver
    ```

7. **Open a Browser and Go To**:

    ```url
    http://127.0.0.1:8000/
    ```

---

## Application Structure

The application consists of two apps: `employee` and `user`. Both apps share a common `base.html` file, which defines the layout of all pages.

- **Database**: The application uses SQLite to store data.
- **Frontend**: The frontend is built using HTML, CSS, and Bootstrap.

---

## Features

### 1. User Login

- Upon launching the application, users are presented with a login interface.
- Unregistered users can register through the "Register" link.
- **Feature**: User authentication (login, registration, logout).

### 2. Display Employee Data

- Shows basic information about employees, including first name, last name, department, and contract type.
- Clicking on an employee's name opens a detailed view with additional information.

### 3. Administrative Privileges

- Administrators can add and delete employees through the admin panel.
- **Feature**: Administrative functions (adding and deleting employees).

### 4. Updating Employee Data

- Users can update employee data through a form, receiving a success message after changes are applied.

### 5. Adding a New Employee

- Users can add new employees through a form on the main page.

### 6. User Profile

- Users can update their own information via the "Profile" page.

### 7. Logout

- Users can log out by clicking "Logout".

---

## Technologies

- **Django** - Web framework for backend
- **SQLite** - Database
- **HTML, CSS, Bootstrap** - Frontend technologies for building the interface
