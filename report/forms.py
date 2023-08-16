from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class ReportForm(FlaskForm):
    """Форма для запроса по имени получателя"""
    report = StringField("Report", validators=[DataRequired()], render_kw={"placeholder": "name"})
