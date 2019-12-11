from flask_wtf import FlaskForm
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

class UserProfileForm(FlaskForm):
    pass