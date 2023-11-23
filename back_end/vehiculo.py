import mysql.connector
class Vehiculo:
    def __init__(self, db):
        self.db = db

    def insert(self,idVehiculo,Tipo_Vehiculo,Modelo_idModelo,año):
        sql = "INSERT INTO vehiculo VALUES (%s,%s,%s,%s)"
        self.db.cursor.execute(sql,(idVehiculo,Tipo_Vehiculo,Modelo_idModelo,año))
        self.db.commit()
          

    def update(self, idVehiculo,Tipo_Vehiculo,Modelo_idModelo,año):
         sql = "UPDATE vehiculo SET Tipo_Vehiculo = %s,Modelo_idModelo = %s,año = %s WHERE idVehiculo = %s"
         self.db.cursor.execute(sql, (idVehiculo,Tipo_Vehiculo,Modelo_idModelo,año))
         self.db.commit()

    def delete(self, idVehiculo):
         sql = "DELETE FROM vehiculo WHERE idVehiculo = %s"
         self.db.cursor.execute(sql, (idVehiculo,))
         self.db.commit()
    
    def get_all_Vehiculos(self):
        try:
            sql = "SELECT * FROM Vehiculo ORDER BY idVehiculo"
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al obtener todos los modelos: {e}")
            return None