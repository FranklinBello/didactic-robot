from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo, ValidationError
from cygnus.models import User

class RegistrationForm(FlaskForm):
    username = StringField  ('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email    = StringField  ('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm  = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit   = SubmitField  ('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already registered.')

class LoginForm(FlaskForm):
    email    = StringField  ('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField ('Remember Me')
    submit   = SubmitField  ('Sign In')

class PostForm(FlaskForm):
    title   = StringField('Title', validators=[DataRequired()])
    body    = TextAreaField('Body', validators=[DataRequired()])

class SearchForm(FlaskForm):
    search  = StringField('SearchBar')
    submit  = SubmitField('SearchBtn')

class NewCourseForm(FlaskForm):
    name = StringField('Course Name')
    description = StringField('Course Description')

class EditProfileForm(FlaskForm):
    username = StringField  ('Username', validators=[Length(min=3, max=20)])
    first_name = StringField('First Name', validators=[Length(min=2, max=20)])
    last_name  = StringField('Last Name', validators=[Length(min=2, max=20)])
    email    = StringField  ('Email', validators=[Email()])
    bio      = TextAreaField('Bio')
    city     = StringField  ('City', validators=[Length(min=2, max=20)])
    state    = StringField  ('State', validators=[Length(min=2, max=20)])
    zip_code = StringField  ('Zip Code', validators=[Length(min=3, max=10)])
    picture  = FileField    ('Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit   = SubmitField  ('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is already taken.')
            elif not username.data.isalnum():
                raise ValidationError('The username must contain only alphanumeric characters.')

    def validate_last_name(self, first_name):
        if not first_name.data.isalpha():
            raise ValidationError('Only use alphabetic characters.')

    def validate_last_name(self, last_name):
        if not last_name.data.isalpha():
            raise ValidationError('Only use alphabetic characters.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is already registered.')

    def validate_zip(self, zip_code):
        if not zip_code.data.isdigit():
            raise ValidationError('Invalid Zip Code')