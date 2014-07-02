from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required

class PriorityForm(Form):
	name = TextField('Name', validators=[Required()])

