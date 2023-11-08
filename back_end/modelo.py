import mysql.connector

class Modelo:
    def __init__(self, db):
        self.db = db

    def insert(self, nombre):
        sql = "INSERT INTO modelo (nombre) VALUES (%s)"
        self.db.cursor.execute(sql, (nombre))
        self.db.commit()

    def update(self, id, nuevo_nombre):
        sql = "UPDATE modelo SET nombre = %s WHERE id = %s"
        self.db.cursor.execute(sql, (nuevo_nombre, id))
        self.db.commit()

    def delete(self, id):
        sql = "DELETE FROM modelo WHERE id = %s"
        self.db.cursor.execute(sql, (id,))
        self.db.commit()
