from flask import Blueprint, render_template, redirect, url_for, request
from mailing.utils import recipient_list, valid_format_file, email_recipient, reading_file
from mailing.forms import MailForm
from tasks.tasks import send_email
from settings_env import smtp_user

mailing_list = Blueprint("mailing", __name__, template_folder="templates", static_folder="static")

_SAVE_PATH_FILE = "mailing/"


@mailing_list.route("/monitoring-list")
def monitoring_recipient():
    """Мониторинг получателей"""
    recipients = recipient_list()
    return render_template("monitoring.html", recipients=recipients)


@mailing_list.route("/mailing", methods=["GET", "POST"])
def send_email_to_recipient():
    """Отправка писем получателям (вложение опционально в формате pdf)"""
    form = MailForm()
    if request.method == "GET":
        return render_template("mailing_form.html", form=form)

    if form.validate_on_submit():
        form_data = request.form.to_dict()
        subject = form_data.get("subject")
        text = form_data.get("text")
        file = request.files.get("file")
        email_list = email_recipient()
        if valid_format_file(file.filename):
            data = reading_file(_SAVE_PATH_FILE, file)
            if not isinstance(data, str):
                file_data = data.get("file_data")
                file_name = data.get("file_name")
                send_email.delay(email_list, smtp_user, subject, text, file_data=file_data, file_name=file_name)
            else:
                send_email.delay(email_list, smtp_user, subject, text)
        else:
            send_email.delay(email_list, smtp_user, subject, text)
    return redirect(url_for("mailing.monitoring_recipient"))
