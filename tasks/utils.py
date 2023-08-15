from sqlalchemy import select
from database.models import Recipient
from database.connect_db import session_maker


def record_update(email):
    """Обновляет записи в таблице"""
    with session_maker() as db_session:
        record = db_session.execute(select(Recipient).where(Recipient.email == email)).scalar()
        record.status = "send"
        record.count_sent += 1
        db_session.commit()
