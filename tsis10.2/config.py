# параметры подключения к базе данных из файла конфигурации ini
from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
#db который будет содержать параметры подключения к базе данных.
    db = {}
    # проверяется, содержит ли файл конфигурации раздел с именем, переданным в аргументе section.
    if parser.has_section(section):
        #если раздел найден, то методом items из объекта parser извлекаются параметры данного раздела.
        params = parser.items(section)
        #параметры раздела перебираются циклом.
        for param in params:
            # для каждого параметра ключ (имя параметра) и значение добавляются в словарь db.
            db[param[0]] = param[1]
    else:
        raise Exception("Error")
    return db