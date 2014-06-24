from flask.ext.sqlalchemy import SQLAlchemy

from .. import db
from . import login_manager

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(80), unique=True)
	password = db.Column(db.String(255))

	def __init__(self, name, password):
		self.name = name
		self.password = password

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False
	 
	def get_id(self):
		return str(self.id)
				 
	def __repr__(self):
		return '<User %r>' % (self.username)

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))
