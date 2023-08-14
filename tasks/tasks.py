import smtplib
from tasks.settings_celery import app_celery
from settings_env import smtp_user, smtp_password, smtp_host, smtp_port
from email.message import EmailMessage
from tasks.utils import reading_file

print(app_celery)


@app_celery.task(queue="email")
def send_email(emails_list, from_email, subject, text, file_path=None):
    """Рассылка писем"""
    try:
        with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
            server.login(smtp_user, smtp_password)
            if file_path:
                data = reading_file(file_path)
                if not isinstance(data, str):
                    file_data = data.get("file_data")
                    file_name = data.get("file_name")
                else:
                    return data
            for email in emails_list:
                msg = EmailMessage()
                msg["From"] = from_email
                msg["To"] = email
                msg["Subject"] = subject
                msg.set_content(text)
                if file_path:
                    msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)
                server.send_message(msg)
            return "Отправка завершена"
    except (smtplib.SMTPException, ValueError) as ex:
        return {"error": f"{ex}"}
