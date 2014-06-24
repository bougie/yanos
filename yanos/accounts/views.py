from flask import render_template, redirect, url_for, jsonify, request

from . import bp
from .forms import RegisterForm, LoginForm
from .core.register import coreRegister
from .core.login import coreLogin
from .core.logout import coreLogout

@bp.route('/')
def index():
	tpl_vars = {
		'page_title': '\_o&lt;~ KOIN KOIN INDEX'
	}
	return render_template('accounts/index.j2', **tpl_vars)

@bp.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(csrf_enabled=False)
	if request.method == 'POST':
		if form.validate_on_submit():
			try:
				connected = coreLogin(
					username=form.username.data,
					password=form.password.data,
					remember_me=form.remember.data
				)
			except Exception as e:
				print(str(e))
				json = {
					'success': False,
					'msg': str(e)
				}
			else:
				if connected:
					json = {
						'success': True,
						'msg': 'Vous etes maintenant connecté',
						'redirect': url_for('accounts.index')
					}
				else:
					json = {
						'success': False,
						'msg': 'Utilisateur ou mot de passe incorrect'
					}
		else:
			json = {
				'success': False,
				'msg': 'Veuillez à remplir correctement le formulaire'
			}

		return jsonify(**json)
	else:
		tpl_vars = {
			'page_title': '\_o&lt;~ KOIN KOIN LOGIN',
			'form': form
		}
		return render_template('accounts/login.j2', **tpl_vars)

@bp.route('/logout')
def logout():
    coreLogout()
    return redirect(url_for('accounts.index'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(csrf_enabled=False)
	if request.method == 'POST':
		if form.validate_on_submit():
			try:
				coreRegister(
					username=form.username.data,
					password=form.password.data,
					password2=form.password2.data
				)
			except Exception as e:
				print(str(e))
				json = {
					'success': False,
					'msg': str(e)
				}
			else:
				json = {
					'success': True,
					'msg': 'Compte crée avec succes',
					'redirect': url_for('accounts.login')
				}
		else:
			json = {
				'success': False,
				'msg': 'Veuillez à remplir correctement le formulaire'
			}

		return jsonify(**json)
	else:
		tpl_vars = {
			'page_title': '\_o&lt;~ KOIN KOIN REGISTER',
			'form': form
		}
		return render_template('accounts/register.j2', **tpl_vars)
