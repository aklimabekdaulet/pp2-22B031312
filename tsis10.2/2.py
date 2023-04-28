import psycopg2
from psycopg2 import Error

connection = None

try:
    # Подключиться к существующей базе данных
    connection = psycopg2.connect(user="aklima",
                                  # пароль, который указали при установке PostgreSQL
                                  password="217MKD",
                                  host="localhost",
                                  port="5432",
                                  database="pp2")

    # Создайте курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # SQL-запрос для создания новой таблицы
    create_table_query = '''
                          INSERT INTO phonebook (ID,NAME,NUMBER) 
                          VALUES 
                          (22B031312,'Aklima','87788816211')
                          '''
    # Выполнение команды: это создает новую таблицу
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")