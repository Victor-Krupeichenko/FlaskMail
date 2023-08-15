import os
from functools import wraps


def file_storage(func):
    """Временное хранение файла и удаление файла после его чтения"""

    @wraps(func)
    def wrapper(save_path_file, file_path, *args, **kwargs):
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
