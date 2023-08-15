from database.connect_db import session_maker
from database.models import Recipient
from sqlalchemy import select
from my_utils import file_storage


def recipient_list():
    """Получает из базы данных всех получателей"""
    try:
        with session_maker() as db_session:
            result = db_session.scalars(select(Recipient)).all()
            return result
    except Exception as ex:
        return {"error": ex}


def email_recipient():
    """Email адреса получателей"""
    try:
        with session_maker() as db_session:
            email_list = db_session.scalars(select(Recipient.email).select_from(Recipient)).all()
            return email_list
    except Exception as ex:
        return f"error: {ex}"


def valid_format_file(file_name):
    """Валидация формата файла"""
    if file_name.endswith(".pdf"):
        return True
    return False


@file_storage
def reading_file(file_path):
    """Читает файл для отправки по email"""
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
            file_name = file.name
            return {"file_data": file_data, "file_name": file_name}
    except Exception as ex:
        return f"error: {ex}"
