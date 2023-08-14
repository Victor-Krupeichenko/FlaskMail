from flask import Blueprint, render_template, redirect, url_for
from mailing_list.utils import recipient_list
from tasks.tasks import send_email
from settings_env import smtp_user, mail_subject, mail_text
mailing_list = Blueprint("mailing_list", __name__, template_folder="templates", static_folder="static")


@mailing_list.route("/monitoring-list")
def monitoring_recipient():
    """Мониторинг получателей"""
    recipients = recipient_list()
    return render_template("monitoring.html", recipients=recipients)


@mailing_list.route("/")
def send_email_to_recipient():
    """Отправка писем получателям"""
    recipients = recipient_list()
    email_list = list()
    for item in recipients:
        email_list.append(item.email)
    send_email.delay(emails_list=email_list, from_email=smtp_user, subject=mail_subject, text=mail_text)
    return redirect(url_for("mailing_list.monitoring_recipient"))
