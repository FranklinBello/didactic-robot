from datetime import datetime
from cygnus import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

studying = db.Table('studying',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), nullable=False),
    db.PrimaryKeyConstraint('user_id', 'course_id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    image_file = db.Column(db.String(16), default='default.jpg')
    city = db.Column(db.String(20))
    state = db.Column(db.String(20))
    zip_code = db.Column(db.String(10))
    bio = db.Column(db.String(140))

    posts = db.relationship('Post', backref='author', lazy=True)

    courses = db.relationship('Course', secondary=studying, backref='student')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    body = db.Column(db.String(140), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Post('{self.title}', '{self.body}', '{self.date_created}')"

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(140), nullable=False)

    def __repr__(self):
        return f"Course('{self.name}', '{self.description}')"

