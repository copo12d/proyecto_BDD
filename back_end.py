import mysql.connector
from mysql.connector import Error
from sys import exit

# Configura la conexión a la base de datos
try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="30412187",
        database="tu_base_de_datos"
    )
    cursor = conn.cursor()
except Error as ex:
    print("Hubo un erro",ex)
finally:
    cursor.close()
    conn.close()
    
# Crea un cursor para interactuar con la base de datos


# Función para insertar datos
def insertar_datos(nombre, edad):
    sql = "INSERT INTO tabla_ejemplo (nombre, edad) VALUES (%s, %s)"
    val = (nombre, edad)
    cursor.execute(sql, val)
    conn.commit()

# Función para actualizar datos
def actualizar_datos(id, nuevo_nombre, nueva_edad):
    sql = "UPDATE tabla_ejemplo SET nombre = %s, edad = %s WHERE id = %s"
    val = (nuevo_nombre, nueva_edad, id)
    cursor.execute(sql, val)
    conn.commit()

# Función para borrar datos
def borrar_datos(id):
    sql = "DELETE FROM tabla_ejemplo WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    conn.commit()



# Cierra el cursor y la conexión a la base de datos


