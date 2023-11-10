import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        try:
            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            if self.conn.is_connected:
                print("conexion exitosa")
                self.cursor = self.conn.cursor()
        except Error as ex:
            print("la conecxion fallo:",ex)

    def close_connection(self):
        try:
            if self.conn.is_connected:
                self.cursor.close()
                self.conn.close()
        except Error as ex:
            print(f"ocurrio un error{ex}")            
    def commit(self):
        try:
            self.conn.commit()
        except Error as ex:
            print(f"Error al hacer commit{ex}")
    
    





