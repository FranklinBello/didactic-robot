from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_assets import Bundle, Environment

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

assets = Environment(app)
#js = Bundle(output='gen/scripts.js')
# assets.register('js_all', js)
# css = Bundle(output='gen/styles.css')
# assets.register('css_all', css)

from cygnus import views, models