import os
from recipient_list_file.handlers import csv_handler, json_handler
from settings_env import save_path_file
from functools import wraps
from database.models import Recipient
from database.connect_db import session_maker


def file_storage(func):
    """Временное хранение файла и удаление файла после его чтения"""

    @wraps(func)
    def wrapper(file_path, *args, **kwargs):
        if file_path:
            save_path = save_path_file
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            temp_file_path = os.path.join(save_path, file_path.filename)
            file_path.save(temp_file_path)
            result = func(temp_file_path, *args, **kwargs)
            os.remove(temp_file_path)
            return result
        return None

    return wrapper


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
