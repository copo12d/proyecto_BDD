import mysql.connector
class Piezas:
    def __init__(self, db):
        self.db = db

    def insert(self, nombre_pieza,id_piezas):
        try:
            sql = "INSERT INTO piezas VALUES (%s,%s)"
            self.db.cursor.execute(sql, (id_piezas,nombre_pieza))
            self.db.commit()
        except mysql.connector.Error as ex:
            print(f"fallo la conecxion {ex}")

    def update(self, id, nuevo_nombre_pieza):
        try:
            sql = "UPDATE piezas SET nombre = %s, componente_id = %s WHERE id = %s"
            self.db.cursor.execute(sql, (nuevo_nombre_pieza, id))
            self.db.commit()
        except mysql.connector.Error as ex:
            print(f"fallo la conecxion {ex}")
            
    def delete(self, id):
        try:
            sql = "DELETE FROM piezas WHERE id = %s"
            self.db.cursor.execute(sql, (id,))
            self.db.commit()
        except mysql.connector.Error as ex:
            print(f"fallo la conecxion {ex}")
            
    def get_all_piezas(self):
        try:
            sql = "SELECT * FROM piezas"
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al obtener todas las piezas: {e}")