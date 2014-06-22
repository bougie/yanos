from flask.ext.sqlalchemy import SQLAlchemy

from .. import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(80), unique=True)
	password = db.Column(db.String(255))
