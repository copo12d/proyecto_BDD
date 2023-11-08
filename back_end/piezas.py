import mysql.connector
class Piezas:
    def __init(self, db):
        self.db = db

    def insert(self, nombre_pieza):
        sql = "INSERT INTO piezas (nombre_pieza) VALUES (%s, %s)"
        self.db.cursor.execute(sql, (nombre_pieza))
        self.db.commit()

    def update(self, id, nuevo_nombre_pieza):
        sql = "UPDATE piezas SET nombre = %s, componente_id = %s WHERE id = %s"
        self.db.cursor.execute(sql, (nuevo_nombre_pieza, id))
        self.db.commit()

    def delete(self, id):
        sql = "DELETE FROM piezas WHERE id = %s"
        self.db.cursor.execute(sql, (id,))
        self.db.commit()
