from flask import render_template, request, redirect, url_for, flash

from cygnus import app, db, bcrypt
from cygnus.forms import RegistrationForm, LoginForm
from cygnus.models import User

from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')
@app.route('/home')
def home():
    return render_template('public/home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data,).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('public/login.html', header='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/coursecatalog', methods=['GET'])
def coursecatalog():
    return render_template('public/coursecatalog.html', title='Course Catalog')

@app.route('/profile', methods=['GET'])
@login_required
def profile():

    return render_template('public/Profile.html', title='Profile')

@app.route('/about')
def about():
    return render_template('public/about.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('public/404.html', title='Not Found')