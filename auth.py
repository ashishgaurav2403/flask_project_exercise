from flask import Blueprint, render_template, redirect, request, url_for

auth = Blueprint('auth', __name__)

@auth.route('/signup')  
def signup():
    return render_template('signup.html')

@auth.route('/signup' , methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    print(email , name, password)
    return redirect(url_for('auth.login'))

@auth.route('/login')
def login(): 
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "This is used to log out."