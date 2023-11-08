import mysql.connector
class Componentes:
    def __init__(self, db):
        self.db = db

    def insert(self, nombre_componente):
        sql = "INSERT INTO componentes (nombre_componente) VALUES (%s)"
        self.db.cursor.execute(sql, (nombre_componente,))
        self.db.commit()

    def update(self, id, nuevo_nombre):
        sql = "UPDATE componentes SET nombre_componente  = %s WHERE id = %s"
        self.db.cursor.execute(sql, (nuevo_nombre, id))
        self.db.commit()

    def delete(self, id):
        sql = "DELETE FROM componentes WHERE id = %s"
        self.db.cursor.execute(sql, (id))
        self.db.commit()
