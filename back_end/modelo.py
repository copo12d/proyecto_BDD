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

    def update(self, Nombre_Modelo,idModelo):
        sql = "UPDATE modelo SET Nombre_Modelo = %s WHERE idModelo = %s"
        self.db.cursor.execute(sql, (Nombre_Modelo,idModelo))
        self.db.commit()

    def delete(self, idModelo):
        sql = "DELETE FROM modelo WHERE idModelo = %s"
        self.db.cursor.execute(sql, (idModelo,))
        self.db.commit()
        
    def get_all_modelos(self):
        try:
            sql = "SELECT * FROM modelo ORDER BY idModelo"
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al obtener todos los modelos: {e}")
            return None
    
    
    def get_all_modelo_names(self):
        try:
            sql = "SELECT Nombre_Modelo FROM modelo ORDER BY Nombre_Modelo"
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            # Extraer los nombres de los resultados y devolverlos como una lista
            return [row[0] for row in result]
        except Exception as e:
            print(f"Error al obtener todos los modelos: {e}")
            return None
        
    def get_componentes_by_modelo(self, nombre_modelo):
        try:
            sql = "SELECT co.Nombre_Componente FROM componentes co JOIN vehiculo ve ON co.Vehiculo_idVehiculo = ve.idVehiculo JOIN modelo mo ON ve.Modelo_idModelo = mo.idModelo WHERE mo.Nombre_Modelo = %s"
            self.db.cursor.execute(sql, (nombre_modelo,))
            result = self.db.cursor.fetchall()
            return [row[0] for row in result]
        except Exception as e:
            print(f"Error al obtener componentes por modelo: {e}")
            return None
            
