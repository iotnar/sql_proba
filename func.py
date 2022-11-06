# This Python file uses the following encoding: utf-8

from conf import password
from mysql.connector import connect, Error


def conn(host,user,database): #подключение к базе данных на сервере
    try:
        with connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=database,
        ) as connection:
            print("Подключение к MYSQL - ok")
            print("Вы подключились к базе --"+database+"--")
            show_db_query = "SHOW DATABASES"
            with connection.cursor() as cursor:

                cursor.execute(show_db_query)
                print("Список баз на "+host)
                for row in cursor:
                    print(row)
    except Error as e:
        print(e)

def show_db(database): #подключение к базе данных на сервере
    try:
        connection=connect()
        show_db_query = "SELECT * FROM zagruzka LIMIT 5"
        cursor=connection.cursor()
        cursor.execute(show_db_query)
        result = cursor.fetchall()
        for row in result:
            print(row)

    except Error as e:
        print(e)