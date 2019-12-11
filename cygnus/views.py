from flask import render_template, request, redirect, url_for, flash

from cygnus import app, db, bcrypt
from cygnus.forms import RegistrationForm, LoginForm
from cygnus.models import User

from flask_login import login_user

@app.route('/')
@app.route('/home')
def home():
    return render_template('public/home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data,).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    flash(f'{form.errors}', 'danger')
    return render_template('public/login.html', header='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, 
                    email=form.email.data, 
                    password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        flash('Your account was created', 'success')
        return redirect(url_for('login'))
    return render_template('public/register.html', title='Register', form=form)

@app.route('/coursecatalog', methods=['GET'])
def courseCatalog():
    return render_template('public/coursecatalog.html', title='Course Catalog')

@app.route('/profile', methods=['GET'])
def Profile():
    return render_template('public/Profile.html', title='Profile')

@app.route('/about')
def about():
    return render_template('public/about.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('public/404.html', title='Not Found')