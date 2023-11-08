import mysql.connector
class Materiales:
    def __init(self, db):
        self.db = db

    def insert(self, nombre_material):
        sql = "INSERT INTO materiales (nombre_material) VALUES (%s)"
        self.db.cursor.execute(sql, (nombre_material))
        self.db.commit()

    def update(self, id, nuevo_nombre):
        sql = "UPDATE materiales SET nombre = %s, pieza_id = %s WHERE id = %s"
        self.db.cursor.execute(sql, (nuevo_nombre,id))
        self.db.commit()

    def delete(self, id):
        sql = "DELETE FROM materiales WHERE id = %s"
        self.db.cursor.execute(sql, (id,))
        self.db.commit()
