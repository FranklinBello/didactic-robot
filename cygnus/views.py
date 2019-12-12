import os
import secrets
from PIL import Image

from flask import render_template, request, redirect, url_for, flash

from cygnus import app, db, bcrypt
from cygnus.forms import RegistrationForm, LoginForm, EditProfileForm
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

@app.route('/profile')
@login_required
def profile():
    image_file = url_for('static', filename='img/profile_pics/' + current_user.image_file)
    return render_template('public/profile.html', title='Profile', image_file=image_file)

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/img/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn

@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def editprofile():
    form = EditProfileForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.city = form.city.data
        current_user.state = form.state.data
        current_user.zip_code = form.zip_code.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.city.data = current_user.city
        form.state.data = current_user.state
        form.zip_code.data = current_user.zip_code
    return render_template('public/editprofile.html', title='Edit Profile', form=form)

@app.route('/coursecatalog', methods=['GET'])
def coursecatalog():
    return render_template('public/coursecatalog.html', title='Course Catalog')

@app.route('/about')
def about():
    return render_template('public/about.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('public/404.html', title='Not Found')