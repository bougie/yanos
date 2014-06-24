from flask.ext.login import logout_user

from ..models import User

def coreLogout():
    logout_user()
