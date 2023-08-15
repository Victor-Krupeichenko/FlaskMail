from recipient_list_file.handlers import csv_handler, json_handler
from my_utils import file_storage
from database.models import Recipient
from database.connect_db import session_maker


@file_storage
def validate_file(file, *keys, number_keys=None):
    """Проверка файла"""

    if file.endswith(".csv"):
        return csv_handler(file, *keys, number_keys=number_keys)
    elif file.endswith(".json"):
        return json_handler(file, *keys, number_keys=number_keys)
    return None


def inserting_data(data):
    """Вставка данных в базу данных"""

    with session_maker() as db_session:
        db_session.bulk_insert_mappings(Recipient, data)
        db_session.commit()
