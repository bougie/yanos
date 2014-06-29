from flask import render_template, redirect, url_for, jsonify, request

from . import bp
#from .forms import 
#from .core. import 

@bp.route('/tasks')
def index():
	tpl_vars = {
		'page_title': '\_o&lt;~ KOIN KOIN TASKS'
	}
	return render_template('tasks/index.j2', **tpl_vars)
