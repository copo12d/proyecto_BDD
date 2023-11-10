import mysql.connector

class Modelo:
    def __init__(self, db):
        self.db = db

    def insert(self, idModelo,Nombre_Modelo,año,Marca_idMarca):
        sql = "INSERT INTO modelo VALUES (%s,%s,%s,%s)"
        self.db.cursor.execute(sql, (idModelo,Nombre_Modelo,año,Marca_idMarca))
        self.db.commit()

    def update(self, idModelo, Nombre_Modelo,año):
        sql = "UPDATE modelo SET Nombre_Modelo = %s,año = %s WHERE idModelo = %s"
        self.db.cursor.execute(sql, (Nombre_Modelo,año,idModelo))
        self.db.commit()

    def delete(self, idModelo):
        sql = "DELETE FROM modelo WHERE idModelo = %s"
        self.db.cursor.execute(sql, (idModelo,))
        self.db.commit()
