import mysql.connector
class Marca:
    def __init__(self, db):
        self.db = db

    def insert(self,nombre_marca):
        sql = "INSERT INTO modelo (nombre) VALUES (%s)"
        self.db.cursor.execute(sql, (nombre_marca))
        self.db.commit()
          

    def update(self, id, nuevo_nombre_marca):
         sql = "UPDATE marca SET nombre = %s WHERE id = %s"
         self.db.cursor.execute(sql, (nuevo_nombre_marca, id))
         self.db.commit()

    def delete(self, id):
         sql = "DELETE FROM marca WHERE id = %s"
         self.db.cursor.execute(sql, (id))
         self.db.commit()