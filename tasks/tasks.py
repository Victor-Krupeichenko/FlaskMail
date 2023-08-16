import smtplib
import os
from tasks.settings_celery import app_celery
from settings_env import smtp_user, smtp_password, smtp_host, smtp_port
from email.message import EmailMessage
from tasks.utils import record_update
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus.paragraph import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO


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


@app_celery.task(queue="reports")
def create_pdf_report(recipient_list, save_folder_file, file_name):
    """Создание pdf файла"""
    output = BytesIO()
    doc = SimpleDocTemplate(output, pagesize=letter)
    data = [["#", "Name", "Email", "Quantity of Messages", "Status"]]

    for idx, recipient in enumerate(recipient_list, start=1):
        data.append(
            [
                str(idx), recipient.get("name"), recipient.get("email"), str(recipient.get("count_sent")),
                recipient.get("status")
            ]
        )

    elements = list()
    styles = getSampleStyleSheet()
    title = "<para align=center spaceb=20><b>List of Recipients</b></para>"
    elements.append(Paragraph(title, styles['Title']))

    table = Table(data)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

    elements.append(table)
    doc.build(elements)

    output_path = os.path.join(save_folder_file, file_name)

    with open(output_path, "wb") as f:
        f.write(output.getvalue())

    return f"{file_name} create"
