from datetime import datetime


def convert_string_data_to_datetime(data):
    convert_data = datetime.strftime(data, "%Y-%m-%d %H:%M:%S")
    return convert_data
