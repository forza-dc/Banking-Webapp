from flask import render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from app import app, db, login_manager  # Import 'app' here

# Define your routes and logic below

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# Add more routes as needed
