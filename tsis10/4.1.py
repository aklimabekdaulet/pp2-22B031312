import psycopg2
from psycopg2 import Error
l, o = int(input()), int(input())
try:
    connection = psycopg2.connect(
        host='localhost', 
        database='postgres',
        user='postgres',
        password='sadaa197688630'
    )

    cursor = connection.cursor()
    # хранимая процедура
    cursor.callproc('pagi2', (l, o,))
    result = cursor.fetchall()
    for i in result:
        print(*i)

except (Exception, Error) as error:
    print("ERROR", error)
finally:
    if connection:
        cursor.close()
        connection.close()