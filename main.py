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
    a_borar = f"DELETE TABLE {tabla}"


connection = create_server_connection("localhost", "root", "Juan2018")

create_database_query = "CREATE DATABASE Twiin"
# create_database(connection, create_database_query)

create_local_table = """
CREATE TABLE Local (
  local_id INT PRIMARY KEY,
  local_name VARCHAR(40) NOT NULL,
  clothes_1 VARCHAR(10) NOT NULL,
  clothes_2 VARCHAR(10),
  asociado_desde DATE,
  tax_id INT UNIQUE,
  phone_no VARCHAR(20)
  );
 """


connection = create_db_connection("localhost", "root", "Juan2018", "Twiin")  # Connect to the Database
# execute_query(connection, create_local_table)  # Execute our defined query
# execute_query(connection, elim_tabla("teacher"))

create_twiin_table = """
CREATE TABLE twiin (
  twiin_id INT PRIMARY KEY,
  tax_id INT UNIQUE
  );
 """

create_client_table = """
CREATE TABLE twiin (
  client_id INT PRIMARY KEY,
  client_name VARCHAR(40) NOT NULL,
  e-mail VARCHAR(60) NOT NULL,
  medida_cintura VARCHAR(10) NOT NULL,
  medida_cadera VARCHAR(10) NOT NULL,
  talle_1 INT,
  altura VARCHAR(10)
 );
"""

create_ropa_table = """
CREATE TABLE course (
  ropa_id INT PRIMARY KEY,
  ropa_name VARCHAR(40) NOT NULL,
  tela VARCHAR(40) NOT NULL,
  medida_cintura VARCHAR(10),
  medida_cadera VARCHAR(10),
  medida_largo VARCHAR(10),
  medida_a_largo VARCHAR(10),
  medida_a_ancho VARCHAR(10),
  medida_6 VARCHAR(10),
  talle_b INT,
  talle_a INT,
  es_elastico BOOLEAN,
  local INT
);
"""

execute_query(connection, create_client_table)
execute_query(connection, create_twiin_table)

# Creo relacion entre las tablas

alter_client = """
ALTER TABLE client
ADD FOREIGN KEY(client)
REFERENCES local(local_id)
ON DELETE SET NULL;
"""

alter_ropa = """
ALTER TABLE ropa
ADD FOREIGN KEY(local)
REFERENCES local(local_id)
ON DELETE SET NULL;
"""

alter_ropa_again = """
ALTER TABLE ropa
ADD FOREIGN KEY(local)
REFERENCES local(local_id)
ON DELETE SET NULL;
"""

create_compraropa_table = """
CREATE TABLE compra_ropa (
  client_id INT,
  ropa_id INT,
  PRIMARY KEY(client_id, ropa_id),
  FOREIGN KEY(client_id) REFERENCES client(client_id) ON DELETE CASCADE,
  FOREIGN KEY(ropa_id) REFERENCES ropa(ropa_id) ON DELETE CASCADE
);
"""

execute_query(connection, alter_client)
execute_query(connection, alter_ropa)
execute_query(connection, alter_ropa_again)
execute_query(connection, create_compraropa_table)