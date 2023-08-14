from database.connect_db import session_maker
from database.models import Recipient
from sqlalchemy import select


def recipient_list():
    """Получает из базы данных всех получателей email"""
    try:
        with session_maker() as db_session:
            result = db_session.scalars(select(Recipient)).all()
            return result
    except Exception as ex:
        return {"error": ex}


