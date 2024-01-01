# Python Banking App

Welcome to the Python Banking App! This simple web application allows users to manage their bank accounts, view balances, perform transactions, and more.

## Introduction

This project is built using the Flask web framework for the backend and HTML, CSS, and Bootstrap for the frontend. It provides basic banking functionalities, including user authentication, account management, and transaction handling.

## Project Structure

The project is organized as follows:

- **app/**: This directory contains the core application code.
  - **\_\_init\_\_.py**: Initializes the Flask application and sets up configurations.
  - **config.py**: Defines configuration settings, such as the secret key and database URI.
  - **forms.py**: Contains forms used for user input (e.g., login form).
  - **models.py**: Defines database models (e.g., User, Account, Transaction).
  - **routes.py**: Implements the application routes and logic.
  - **templates/**: Stores HTML templates for different views.
  - **static/**: Contains static assets such as CSS and JavaScript files.

- **run.py**: This script is used to run the Flask application.

## How to Run the Project

Follow these steps to run the Python Banking App:

1. **Set Up Virtual Environment:**
   ```bash
   python -m venv venv


Activate Virtual Environment:

On Windows:

venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate
Install Dependencies:


pip install -r requirements.txt
Run the Application:


python run.py
Access the App:
Open your web browser and navigate to http://127.0.0.1:5000/

Notes
Ensure that you have Python installed on your system.
The app uses a simple SQLite database by default. If you want to switch to a more robust database like PostgreSQL, update the SQLALCHEMY_DATABASE_URI in config.py accordingly.