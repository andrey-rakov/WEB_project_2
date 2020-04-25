from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class AddTopicForm(FlaskForm):
    topic_title = StringField('Наименование темы', validators=[DataRequired()])
    submit = SubmitField('Запомнить')
