from flask import g
from sqlalchemy import exc
from werkzeug.security import generate_password_hash, check_password_hash

from ... import db
from ..models import User

def corePassword(old_password, password, password2):
	if password != password2:
		raise Exception('passwords have to be equals')

	password = generate_password_hash(password)

	try:
		usr = User.query.filter_by(name=g.user.name).first()
	except Exception as e:
		print(str(e))
		raise Exception('unknown error')
	else:
		if usr is not None:
			if check_password_hash(usr.password, old_password):
				usr.password = generate_password_hash(password)
				db.session.commit()
			else:
				raise Exception('wrong current password')
		else:
			raise Exception('unable to get user')
