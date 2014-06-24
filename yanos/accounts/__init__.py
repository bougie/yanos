from flask import Blueprint, g
from flask.ext.login import LoginManager, current_user

from .. import app

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'accounts.login'

@app.before_request
def before_request():
	g.user = current_user

bp = Blueprint(
	'accounts',
	__name__,
	template_folder='templates',
	static_folder='static'
)

from .views import *
