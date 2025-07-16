from flask import render_template,request,flash,redirect,url_for
from models import User,db # models.py se User model import karega 
from werkzeug.security import generate_password_hash, check_password_hash # password hashing ke liye, aurpassword verification ke liye
from app import app  # app.py se Flask instance import karega

@app.route('/')
def home():
    return render_template('index.html')  # templates/index.html render karega

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        flash('Username and Password are required!')
        return redirect(url_for('login'))

    user = User.query.filter_by(name=username).first()

    if not user:
        flash('User not found!')
        return redirect(url_for('login'))
    
    if not check_password_hash(user.password, password):
        flash('Incorrect Password!')
        return redirect(url_for('login'))
    
    return redirect(url_for('home'))  # Successful login, redirect to home page




@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

#doing this from lEctur no.3 
# reason ki ye sare code krne ka ye h ki register krete waqt kaun si fields required hai
  
@app.route('/register',methods=['POST'])
def register_post():
    username = request.form.get('username')
    password= request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    email = request.form.get('email')

    if not username or not password or not confirm_password or not email:
        flash('All fields are required!')
        return redirect (url_for('register'))
    
    if password != confirm_password:
        flash('Passwords do not match!')
        return redirect (url_for('register'))
    if len(password) < 6:
        flash('Password must be at least 6 characters long!')
        return redirect (url_for('register'))
    if len(username) < 3:
        flash('Username must be at least 3 characters long!')
        return redirect (url_for('register'))
    
    existing_user =User.query.filter_by(name=username).first()
    if existing_user:
        flash('Username already exists!')
        return redirect(url_for('register'))
    
    password_hash=generate_password_hash(password)
    
    new_user = User(name=username, email=email, password=password_hash) # kyki password ek security wali chij hto isko hash krte hai
    db.session.add(new_user)   #adding new user to the database
    db.session.commit()
    return redirect(url_for('login'))             

   