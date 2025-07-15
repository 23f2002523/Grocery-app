from flask import render_template
from app import app  # app.py se Flask instance import karega

@app.route('/')
def home():
    return render_template('index.html')  # templates/index.html render karega

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')