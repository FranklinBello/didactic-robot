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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('public/register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@cygnus.com' and form.password.data == 'password':
            return redirect(url_for('dashboard'))
    return render_template('public/login.html', title='Login', form=form)

@app.route('/dashboard')
def dashboard():
    return 'Dashboard'