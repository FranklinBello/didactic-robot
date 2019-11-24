from flask import render_template, redirect
from cygnus import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('public/home.html')

@app.route('/about')
def about():
    return render_template('public/about.html')

@app.route('/sign-up')
def sign_up():
    return 'Create an account'

@app.route('/log-in')
def log_in():
    return 'Welcome back'