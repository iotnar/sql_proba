q0 = """SELECT * FROM zagruzka """
q1 = """SELECT * FROM zagruzka_1 """
q2 = """SELECT * FROM zagruzka_2 """
q3 = """SELECT * FROM  starshie"""



create_starshie_table = """
CREATE TABLE starshie (
    id INT PRIMARY KEY,
   first_name VARCHAR(40) NOT NULL,
   last_name VARCHAR(40) NOT NULL,
   status VARCHAR(10) NOT NULL
  );
 """
