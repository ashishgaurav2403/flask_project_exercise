from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/signup')  
def signup():
    return "This page wil be used to sign up users."

@auth.route('/login')
def login(): 
    return "This page will be used to log in users."

@auth.route('/logout')
def logout():
    return "This is used to log out."