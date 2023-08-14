import csv
import json


def csv_handler(file, *keys, number_keys=None):
    """Обработчик csv-файла"""
    json_lists = list()
    with open(file, "r", encoding="utf-8") as my_file:
        for row in csv.DictReader(my_file):
            if number_keys and len(row) != number_keys:
                continue
            if keys and not all(key in row for key in keys):
                continue
            json_lists.append(row)
        return json_lists


def json_handler(file, *keys, number_keys=None):
    """Обработчик json-файла"""
    json_list = list()
    with open(file, "r", encoding="utf-8") as my_file:
        data = json.load(my_file)
        if isinstance(data, list):
            for row in data:
                if number_keys is not None and len(row) != number_keys:
                    continue
                if keys and not any(key in row for key in keys):
                    continue
                json_list.append(row)
        else:
            return None
    return json_list
