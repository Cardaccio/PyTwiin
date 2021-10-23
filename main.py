import mysql.connector
from mysql.connector import Error
#import panda as pd


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


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
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


def elim_tabla (tabla):
    a_borar = f"DROP TABLE {tabla}"


connection = create_server_connection("localhost", "root", "Juan2018")

create_database_query = "CREATE DATABASE Twiin"
# create_database(connection, create_database_query)


connection = create_db_connection("localhost", "root", "Juan2018", "Twiin")  # Connect to the Database
# execute_query(connection, create_local_table)  # Execute our defined query
#execute_query(connection, elim_tabla("local"))

create_local_table = """
CREATE TABLE local (
  local_id INT PRIMARY KEY,
  local_name VARCHAR(40) NOT NULL,
  asociado_desde DATE,
  tax_id INT UNIQUE,
  phone_no VARCHAR(20),
  ropa INT,
  cliente INT
  );
 """

create_twiin_table = """
CREATE TABLE twiin (
  twiin_id INT PRIMARY KEY,
  tax_id INT UNIQUE,
  local INT
  );
 """

create_cliente_table = """
CREATE TABLE cliente (
  cliente_id INT PRIMARY KEY,
  cliente_name VARCHAR(40) NOT NULL,
  e_mail VARCHAR(40) NOT NULL,
  cintura INT,
  cadera INT,
  talle_1 INT,
  altura INT
 );
"""

create_ropa_table = """
CREATE TABLE ropa (
  ropa_id INT PRIMARY KEY,
  ropa_name VARCHAR(40) NOT NULL,
  tela VARCHAR(40) NOT NULL,
  medida_cintura INT,
  medida_cadera INT,
  medida_largo INT,
  talle INT,
  es_elastico BOOLEAN,
  local INT
);
"""

#execute_query(connection, create_cliente_table)
#execute_query(connection, create_twiin_table)
#execute_query(connection, create_ropa_table)
#execute_query(connection, create_local_table)

# Creo relacion entre las tablas


alter_twiin = """
ALTER TABLE twiin
ADD FOREIGN KEY(local)
REFERENCES local(local_id)
ON DELETE SET NULL;
"""

alter_ropa = """
ALTER TABLE ropa
ADD FOREIGN KEY(local)
REFERENCES local(local_id)
ON DELETE SET NULL;
"""

alter_local = """
ALTER TABLE local
ADD FOREIGN KEY(ropa)
REFERENCES ropa(ropa_id)
ON DELETE SET NULL;
"""

alter_local_again = """
ALTER TABLE local
ADD FOREIGN KEY(cliente)
REFERENCES cliente(cliente_id)
ON DELETE SET NULL;
"""

create_compraropa_table = """
CREATE TABLE compra_ropa (
  cliente_id INT,
  ropa_id INT,
  PRIMARY KEY(cliente_id, ropa_id)
);
"""

#execute_query(connection, alter_twiin)
#execute_query(connection, alter_ropa)
#execute_query(connection, alter_local_again)
#execute_query(connection, alter_local)
#execute_query(connection, create_compraropa_table)


# Populamos las tablas


pop_cliente = """
INSERT INTO cliente VALUES
(101, 'Lucia Gomez', 'lilugomezescola@gmail.com', 60, 90, 24, 162),
(102, 'Solana Auriti', 'soliauriti@gmail.com', 65, 95, 26, 168),
(103, 'Adriana Gomez', 'dermobyadri@gmail.com', 80, 100, 30, 164),
(104, 'Matina Brusca', 'marbrusca@gmail.com', 75, 95, 28, 160),
(105, 'Paula Perez', 'paulita33@gmail.com', 115, 125, 40, 166);
"""

pop_local = """
INSERT INTO local VALUES
(101, 'Cardaccio','2021-10-02', 20925, 247857576, 11,102),
(102, 'Edgar', '2021-10-18', 301455, 1145885523, 11,103);
"""

pop_ropa = """
INSERT INTO ropa VALUES
(11, 'Jean Amy 24','Spandex', 62, 95, 100, 24, TRUE, 101),
(12, 'Jean Amy 26','Spandex', 66, 99, 100, 26, TRUE, 101),
(13, 'Jean Amy 28','Spandex', 75, 105, 103, 28, TRUE, 101),
(14, 'Jean Amy 30','Spandex', 80, 110, 105, 30, TRUE, 101),
(15, 'Jean Amy 32','Spandex', 85, 120, 105, 32, TRUE, 101);
"""

pop_twiin = """
INSERT INTO twiin VALUES
(101, 30575,0);
"""

pop_compraropa = """
INSERT INTO compra_ropa VALUES
(101, 11,101),
(102, 12, 101),
(102, 13, 101),
(103, 14, 101),
(104, 13, 101);
"""

#execute_query(connection, pop_cliente)
#execute_query(connection, pop_local)
##execute_query(connection, pop_twiin)
#execute_query(connection, pop_ropa)
execute_query(connection, pop_compraropa)

