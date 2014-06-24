from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required

class RegisterForm(Form):
	username = TextField('Login', validators=[Required()])
	password = PasswordField('Password', validators=[Required()])
	password2 = PasswordField('Password2', validators=[Required()])

class LoginForm(Form):
	username = TextField('Login', validators=[Required()])
	password = PasswordField('Password', validators=[Required()])
	remember = BooleanField('Remember')
