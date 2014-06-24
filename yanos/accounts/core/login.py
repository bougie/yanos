from sqlalchemy import exc
from werkzeug.security import check_password_hash
from flask.ext.login import login_user, current_user 

#from ... import db
from ..models import User

def coreLogin(username, password, remember_me = False):
	try:
		registered_user = User.query.filter_by(
			name=username
		).first()
	except Exception as e:
		print(str(e))
		return False
	else:
		if registered_user is not None:
			if check_password_hash(
				    registered_user.password,
				    password):
				login_user(
					registered_user,
					remember = remember_me)
				return True

	return False
