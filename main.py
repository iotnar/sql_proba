# This Python file uses the following encoding: utf-8



import mysql.connector


from getpass import getpass
from mysql.connector import connect, Error


from conf import host,user,password,database,base
from func import conn,show_db,execute_query
from qyery import q3,create_starshie_table



try:
    connection=conn(host,user,database)
    #execute_query(connection,create_starshie_table)
    results=show_db(connection,q3)
    for result in results:
        print(result)
except Error as err:
    print(f"Error: '{err}'")