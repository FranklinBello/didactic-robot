from flask import render_template, redirect, url_for
from cygnus import app
from cygnus.forms import RegistrationForm, LoginForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('public/home.html')

@app.route('/about')
def about():
    return render_template('public/about.html')

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('log_in'))
    return render_template('public/sign-up.html', title='Sign Up', form=form)

@app.route('/log-in', methods=['GET', 'POST'])
def log_in():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@cygnus.com' and form.password.data == 'password':
            return redirect(url_for('dashboard'))
    return render_template('public/log-in.html', title='Log In', form=form)

@app.route('/dashboard')
def dashboard():
    return 'Dashboard'