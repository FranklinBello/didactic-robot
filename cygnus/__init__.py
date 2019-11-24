from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'dev',
    SQLAlchemy_DATABASE_URI = 'sqlite:///site.db',
)
db = SQLAlchemy(app)

from cygnus import controllers