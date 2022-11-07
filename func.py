# This Python file uses the following encoding: utf-8

import mysql.connector
from mysql import connector
from mysql.connector import Error

from conf import host,user,password,database
from mysql.connector import connect, Error


def conn(host,user,database): #подключение к базе данных на сервере
    connection = None
    try:
        connection = connector.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=database,
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def show_db(connection,base):

    try:
        b=base
        show_db_query = "SELECT * FROM "+b +" limit 6"
        print(show_db_query)
        with connection.cursor() as cursor:
            cursor.execute(show_db_query)
            result = cursor.fetchall()
            for row in result:
                print(row)

    except Error as e:
        print(e)

        #     # show_db_query = "SHOW DATABASES"
        #     # with connection.cursor() as cursor:
        #     #
        #     #     cursor.execute(show_db_query)
        #     #     print("Список баз на "+host)
        #     #     for row in cursor:
        #     #         print(row)