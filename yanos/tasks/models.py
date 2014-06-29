from flask.ext.sqlalchemy import SQLAlchemy

from .. import db

class Priority(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(80), unique=True)

class Status(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(80), unique=True)

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(255))
	description = db.Column(db.String(255))

	priority_id = db.Column(db.Integer, db.ForeignKey('priority.id'))
	status_id = db.Column(db.Integer, db.ForeignKey('status.id'))
