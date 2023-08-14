from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms.validators import DataRequired
from wtforms import SubmitField


class FileUploadForms(FlaskForm):
    """Форма для загрузки файла в формате csv или json"""
    file = FileField(label="Select CSV or JSON file", validators=[DataRequired()])
    submit = SubmitField(label="Upload File")
