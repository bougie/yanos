from flask import Blueprint

bp = Blueprint(
	'accounts',
	__name__,
	template_folder='templates',
	static_folder='static'
)

from .views import *
