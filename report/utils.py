from sqlalchemy import select
from database.connect_db import session_maker
from database.models import Recipient


def get_report_recipient(name):
    """Получение записи из базы данных"""
    with session_maker() as db_session:
        results = db_session.execute(select(Recipient).filter(Recipient.name == name)).scalars().all()
        return results


def serialize_recipient(recipient):
    """Сериализует получателей"""
    serialize_list = list()
    for r in recipient:
        serialize_list.append(
            {
                'name': r.name,
                'email': r.email,
                'count_sent': r.count_sent,
                'status': r.status
            }
        )
    return serialize_list
