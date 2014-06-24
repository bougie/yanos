from flask import Blueprint
from flask.ext.login import LoginManager

from .. import app

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'accounts.login'

bp = Blueprint(
	'accounts',
	__name__,
	template_folder='templates',
	static_folder='static'
)

from .views import *
