import smtplib
from tasks.settings_celery import app_celery
from settings_env import smtp_user, smtp_password, smtp_host, smtp_port
from email.message import EmailMessage
from tasks.utils import record_update


@app_celery.task(queue="email")
def send_email(emails_list, from_email, subject, text, file_data=None, file_name=None):
    """Рассылка писем"""

    with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
        server.login(smtp_user, smtp_password)
        for email in emails_list:
            try:
                msg = EmailMessage()
                msg["From"] = from_email
                msg["To"] = email
                msg["Subject"] = subject
                msg.set_content(text)
                if file_data and file_name:
                    msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)
                server.send_message(msg)
                record_update(email)
            except (smtplib.SMTPException, ValueError) as ex:
                print(f"error {ex}")
                continue
        return "Отправка завершена"
