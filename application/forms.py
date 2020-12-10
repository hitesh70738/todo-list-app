from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    task_name = StringField('Name of task', validators=[DataRequired()])
    task_description = StringField('Description of task', validators=[DataRequired()])
    submit = SubmitField('Add Task')