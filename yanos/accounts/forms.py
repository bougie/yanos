from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required

class RegisterForm(Form):
	username = TextField('Login', validators=[Required()])
	password = PasswordField('Password', validators=[Required()])
	password2 = PasswordField('Password2', validators=[Required()])