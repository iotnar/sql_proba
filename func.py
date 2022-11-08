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

"""Функция изменения баззы данных """
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

"""Функция чтения из базы данных"""
def show_db(connection,query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")