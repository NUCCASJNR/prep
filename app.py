#!/usr/bin/python3
from flask import Flask, render_template, url_for, request, redirect, flash, get_flashed_messages
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

password = getenv("HBNB_MYSQL_PWD")
user = getenv("HBNB_MYSQL_USER")
host = getenv("HBNB_MYSQL_HOST")
database = getenv("HBNB_MYSQL_DB")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{user}:{password}@{host}:3306/{database}'
app.config['SECRET_KEY'] = getenv("SECRET_KEY") 
db = SQLAlchemy(app)
class NewUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)        
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/login', strict_slashes=False)
#def login():
 #   return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']

        # Check if the email already exists
        existing_user = NewUser.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists. Please use a different email.', 'error')
            return redirect(url_for('signup'))

        # Create a new user
        new_user = NewUser(name=name, email=email, password=password, username=username)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully. You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html', messages=get_flashed_messages())


@app.route('/login', strict_slashes=False)
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Find the user by email
        user = NewUser.query.filter_by(email=email).first()

        if user and user.password == password:
            # Login the user
            login_user(user)
            return render_template('login.html')


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    host = getenv("HBNB_API_HOST")
    port = getenv("HBNB_API_PORT")
    app.run(host=host, port=port, debug=True)
