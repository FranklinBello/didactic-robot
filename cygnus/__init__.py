from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = '4970bca6851d22733d9183f0f5dc467a',
    SQLAlchemy_DATABASE_URI = 'sqlite:///site.db',
)
db = SQLAlchemy(app)

from cygnus import views