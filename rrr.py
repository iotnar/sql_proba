# This Python file uses the following encoding: utf-8

import mysql.connector
from mysql.connector import Error
#import pandas as pd


"""функция подключения к базе данных"""
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

"""функция созданиябазы данных"""
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


connection = create_server_connection("localhost", "root", "root")
create_database_query="CREATE DATABASE sclad2"
create_database(connection,create_database_query)