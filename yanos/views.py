from flask import render_template

from . import app

@app.route('/')
def index():
	tpl_vars = {
		'page_title': '\_o&lt;~ KOIN KOIN INDEX'
	}
	return render_template('index.j2', **tpl_vars)
