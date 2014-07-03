from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class PriorityForm(Form):
	name = TextField('Name', validators=[Required()])

