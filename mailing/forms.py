from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length


class MailForm(FlaskForm):
    """Форма для email"""
    subject = StringField("Subject message", validators=[
        Length(max=150, message="Must not exceed 150 characters"),
        DataRequired()
    ], render_kw={"placeholder": "Subject message"})
    text = TextAreaField("Text message", validators=[DataRequired()],
                         render_kw={"rows": 7, "placeholder": "Text message"})
    file = FileField("file", render_kw={"placeholder": "Select file"})
