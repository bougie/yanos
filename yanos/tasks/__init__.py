from flask import Blueprint

from .. import app

bp = Blueprint(
	'tasks',
	__name__,
	template_folder='templates',
	static_folder='static'
)

from .views import *
