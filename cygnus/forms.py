from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, DateField, SelectMultipleField
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField  ('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email    = StringField  ('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm  = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    # date = DateField('Date')
    # account = SelectField('Account', validators=[DataRequired()], coerce='Unicode', choices=[('1', 'Student'), ('2', 'Tutor')])
    submit   = SubmitField  ('Sign Up')

class LoginForm(FlaskForm):
    email    = StringField  ('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField ('Remember Me')
    submit   = SubmitField  ('Sign In')

class UserProfileForm(FlaskForm):
    # name = StringField('Name')
    # last_name = StringField('Last Name')
    # bio = TextAreaField('Bio')
    # school = StringField('School')
    # campus = StringField('Campus')
    # location = StringField('Location')
    # major = StringField('Major')
    # dob = DateField('Date of Birth')
    # year_graduation = DateField('Graduation Year')
    # course_list = SelectMultipleField()
    # image
    pass

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])

# Add recaptcha field to avoid bots
# If you are a student then submit
#   Unofficial transcripts to verify and one letter of recommendation
# Else
#   Only unofficial transcripts
