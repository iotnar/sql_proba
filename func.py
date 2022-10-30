# This Python file uses the following encoding: utf-8

from conf import password
from mysql.connector import connect, Error


def conn(host,user): #подключение к базе данных на сервере
    try:
        with connect(
                host=host,
                port=3306,
                user=user,
                password=password,
        ) as connection:
            print("Подключение к MYSQL - ok")
            show_db_query = "SHOW DATABASES"
            with connection.cursor() as cursor:

                cursor.execute(show_db_query)
                print("Список баз на "+host)
                for row in cursor:
                    print(row)


    except Error as e:
        print(e)

def conn_db(database): #подключение к базе данных на сервере
    try:
        with connect(
               database=database,
        ) as connection:
            select_db_query = ""
            cursor=connection.cursor()
            print("===++++===")

           # show_db_query = "SHOW DATABASES"
            # with connection.cursor() as cursor:
            #
            #     cursor.execute(show_db_query)
            #     print("Список баз на "+host)
            #     for row in cursor:
            #         print(row)


    except Error as e:
        print(e)