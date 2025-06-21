from flask import render_template
from app import app  # app.py se Flask instance import karega

@app.route('/')
def home():
    return render_template('index.html')  # templates/index.html render karega

