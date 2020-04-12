from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class AddSiteForm(FlaskForm):
    site_address = StringField('URL сайта', validators=[DataRequired()])
    site_name = StringField('Название сайта', validators=[DataRequired()])
    id_topic = IntegerField('Тема сайта')
    site_description = StringField('Описание сайта', validators=[DataRequired()])
    submit = SubmitField('Записать')
