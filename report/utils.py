import os
from sqlalchemy import select
from database.connect_db import session_maker
from database.models import Recipient
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus.paragraph import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO


def get_report_recipient(name):
    """Получение записи из базы данных"""
    with session_maker() as db_session:
        results = db_session.execute(select(Recipient).filter(Recipient.name == name)).scalars().all()
        return results


def create_pdf_report(recipient_list, save_folder_file, file_name):
    """Создание pdf файла"""
    output = BytesIO()
    doc = SimpleDocTemplate(output, pagesize=letter)
    data = [["#", "Name", "Email", "Quantity of Messages", "Status"]]

    for idx, recipient in enumerate(recipient_list, start=1):
        data.append(
            [
                str(idx), recipient.name, recipient.email, str(recipient.count_sent), recipient.status
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
