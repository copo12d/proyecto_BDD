import mysql.connector
class Vehiculo:
    def __init__(self, db):
        self.db = db

    def insert(self,Tipo_Vehiculo,idVehiculo,Modelo_idModelo):
        sql = "INSERT INTO vehiculo VALUES (%s,%s,%s)"
        self.db.cursor.execute(sql,(idVehiculo,Tipo_Vehiculo,Modelo_idModelo))
        self.db.commit()
          

    def update(self, Tipo_Vehiculo,Modelo_idModelo,idVehuculo):
         sql = "UPDATE vehiculo SET Tipo_Vehiculo = %s,Modelo_idModelo = %s WHERE idVehiculo = %s"
         self.db.cursor.execute(sql, (Tipo_Vehiculo,Modelo_idModelo,idVehuculo))
         self.db.commit()

    def delete(self, idVehiculo):
         sql = "DELETE FROM vehiculo WHERE idVehiculo = %s"
         self.db.cursor.execute(sql, (idVehiculo,))
         self.db.commit()
