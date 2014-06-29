from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from .accounts import bp
app.register_blueprint(bp)

from .tasks import bp
app.register_blueprint(bp)

from .views import *
