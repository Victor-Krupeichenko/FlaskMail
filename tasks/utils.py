def reading_file(file_path):
    """Читает файл для отправки по email"""
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
            file_name = file.name
            return {"file_data": file_data, "file_name": file_name}
    except Exception as ex:
        return f"error: {ex}"
