import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
class Modelo:
    def __init__(self, db):
        self.db = db

    def insert(self, idModelo,Nombre_Modelo,Marca_idMarca):
        sql = "INSERT INTO modelo VALUES (%s,%s,%s,%s)"
        self.db.cursor.execute(sql, (idModelo,Nombre_Modelo,Marca_idMarca))
        self.db.commit()

    def update(self, idModelo, Nombre_Modelo,año):
        sql = "UPDATE modelo SET Nombre_Modelo = %s,año = %s WHERE idModelo = %s"
        self.db.cursor.execute(sql, (Nombre_Modelo,año,idModelo))
        self.db.commit()

    def delete(self, idModelo):
        sql = "DELETE FROM modelo WHERE idModelo = %s"
        self.db.cursor.execute(sql, (idModelo,))
        self.db.commit()
        
    def get_all_modelos(self):
        try:
            sql = "SELECT * FROM modelo ORDER BY Nombre_Modelo"
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al obtener todos los modelos: {e}")
            return None
    
        
