from flask.ext.wtf import Form
from wtforms import (StringField, TextAreaField, RadioField,
 BooleanField, SelectField, SubmitField, validators)
from wtforms.validators import Required, Length, Email, Regexp, Optional
from wtforms import ValidationError
from ..models import Task, Category
from wtforms.fields.html5 import DateField
from .. import db
from . import main

class AddTask(Form):
	# C_name=SelectField(u' ', coerce=int)
	name = StringField('Task Name', validators=[Required()])
	due_date = DateField('To be done by?', format='%Y-%m-%d', 
		validators=(validators.Optional(),))
	submit = SubmitField('Add Task')


	
class AddCategory(Form):

	category_name=StringField(' ', validators=[Required()])
	submit = SubmitField('Add Category')

	
	