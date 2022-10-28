# This Python file uses the following encoding: utf-8



import mysql.connector


from getpass import getpass
from mysql.connector import connect, Error
from conf import host,user,password,database

try:
    with connect(
        host=host,
        user=user,
        password=password,
        database=database,
    ) as connection:
        show_db_query = "SHOW DATABASES"
        select_movies_query = "SELECT * FROM zagruzka LIMIT 5"
        print("#################")
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            result = cursor.fetchall()
            for row in result:
                print(row)
        print("#################")

        show_table_query = "DESCRIBE zagruzka"
        with connection.cursor() as cursor:
            cursor.execute(show_table_query)
            # Fetch rows from last executed query
            result = cursor.fetchall()
            for row in result:
                print(row)

            write_to_bd = """
            INSERT INTO zagruzka
            (id, name, sername, status)
            VALUES ( %s, %s, %s ,%s) """
            reviewers_records = [
                ("1", "Chaitanya", "Baweja", "user"),
                ("2", "Mary", "Cooper", "user"),
                ("3", "John", "Wayne", "user"),
                ("4", "Thomas", "Stoneman", "user"),
                ("5", "Penny", "Hofstadter", "user"),
                ("6", "Mitchell", "Marsh", "user"),
                ("7", "Wyatt", "Skaggs", "user"),
                ("8", "Andre", "Veiga", "user"),
                ("9", "Sheldon", "Cooper", "user"),
                ("10", "Kimbra", "Masters", "user"),
                ("11", "Kat", "Dennings", "user"),
                ("12", "Bruce", "Wayne", "master"),
                ("13", "Domingo", "Cortes", "user"),
                ("14", "Rajesh", "Koothrappali", "user"),
                ("15", "Ben", "Glocker", "user"),
                ("16", "Mahinder", "Dhoni", "user"),
                ("17", "Akbar", "Khan", "user"),
                ("18", "Howard", "Wolowitz", "user"),
                ("19", "Pinkie", "Petit", "user"),
                ("20", "Gurkaran", "Singh", "user"),
                ("21", "Amy", "Farah Fowler", "user"),
                ("22", "Marlon", "Crafford", "user"),
            ]
            with connection.cursor() as cursor:
                cursor.executemany(write_to_bd, reviewers_records)
                connection.commit()
        with connection.cursor() as cursor:
            delete_query = "DELETE FROM zagruzka WHERE status = 'master'"
            cursor.execute(delete_query)
            connection.commit()


        show_db_query = "SHOW DATABASES"
        select_movies_query = "SELECT * FROM zagruzka "
        print("111111")
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            result = cursor.fetchall()
            for row in result:print(row)


            #print("#################")
        # with connection.cursor() as cursor:
        #     cursor.execute(select_movies_query)
        #     result = cursor.fetchall()
        #     for row in result:
        #         print(row)
except Error as e:
    print(e)