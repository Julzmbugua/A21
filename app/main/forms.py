from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError


class AddTask(Form):
    name = StringField('Task Category Placeholder', validators=[Required()])
    submit = SubmitField('Add Task')