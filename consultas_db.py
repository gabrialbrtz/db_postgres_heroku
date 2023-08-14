from postgress_connector import PostgresConnector

# Instancia al conector

connector = PostgresConnector()

# Conexión a la base de datos

connection = connector.db_connection()

# Creamos un cursor

cursor = connection.db_connection()

# Puedes hacer varias sentencias como una consulta select

cursor.execute("SELECT * FROM tabla_1;")

# Consulta SQL para crear una vista

create_view_query = """
    CREATE OR REPLACE VIEW mi_vista AS
    SELECT columna1, columna2
    FROM mi_tabla
    WHERE columna1 = 'valor';
"""

# Una vez realizados los cambios en la BD cerramos el cursor y la conexion

connection.commit()
cursor.close()
connection.close()
