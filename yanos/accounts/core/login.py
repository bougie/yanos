from sqlalchemy import exc
from werkzeug.security import generate_password_hash
from flask.ext.login import login_user, current_user 

from ... import db
from ..models import User

def coreLogin(username, password, remeber_me = False):
	try:
		registered_user = User.query.filter_by(
			username=username,
			password=password
		).first()
	except:
		return False
	else:
		if registered_user is not None:
			login_user(registered_user, remember = remember_me)
			return True

	return False
