from sqlalchemy import exc
from werkzeug.security import generate_password_hash

from ... import db
from ..models import User

def coreRegister(username, password, password2):
	if password != password2:
		raise Exception('passwords have to be equals')

	password = generate_password_hash(password)

	try:
		usr = User(name=username, password=password)

		db.session.add(usr)
		db.session.commit()
	except exc.IntegrityError as e:
		db.session.rollback()
		raise Exception('username is already in use')
	except:
		db.session.rollback()
		raise Exception('unknown error')
