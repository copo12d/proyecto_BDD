import mysql.connector
class Piezas:
    def __init__(self, db):
        self.db = db

    def insert(self, nombre_pieza,id_piezas):
        try:
            sql = "INSERT INTO piezas VALUES (%s,%s,%s)"
            self.db.cursor.execute(sql, (id_piezas,nombre_pieza))
            self.db.commit()
        except mysql.connector.Error as ex:
            print(f"fallo la conecxion {ex}")

    def update(self, id_Piezas, Nombre_Pieza,descripcion):
        try:
            sql = "UPDATE piezas SET Nombre_Pieza = %s, descripcion = %s  WHERE id_Pieza = %s"
            self.db.cursor.execute(sql, (id_Piezas,Nombre_Pieza,descripcion ))
            self.db.commit()
        except mysql.connector.Error as ex:
            print(f"fallo la conecxion {ex}")
            
    def delete(self, id_Pieza):
        try:
            sql = "DELETE FROM piezas WHERE id_pieza = %s"
            self.db.cursor.execute(sql, (id_Pieza,))
            self.db.commit()
        except mysql.connector.Error as ex:
            print(f"fallo la conecxion {ex}")
            
    def get_all_piezas(self):
        try:
            sql = "SELECT * FROM piezas"
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            print(f"Error al obtener todas las piezas: {e}")
    
    
            
    