
# import main
#
# q = str(main.name_tb_bd)
q0 = """SHOW TABLES """
q1 = """SELECT * FROM """
q2 = """select * from  """
q3 = """SELECT * FROM  starshie"""



create_starshie_table = """
CREATE TABLE starshie (
    id INT PRIMARY KEY,
   first_name VARCHAR(40) NOT NULL,
   last_name VARCHAR(40) NOT NULL,
   status VARCHAR(10) NOT NULL
  );
 """
