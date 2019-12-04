from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField  ('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email    = StringField  ('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm  = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit   = SubmitField  ('Sign Up')

class LoginForm(FlaskForm):
    email    = StringField  ('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField ('Remember Me')
    submit   = SubmitField  ('Sign In')

class UserProfileForm(FlaskForm):
    pass

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])