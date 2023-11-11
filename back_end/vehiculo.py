import mysql.connector
class Vehiculo:
    def __init__(self, db):
        self.db = db

    def insert(self,Tipo_Vehiculo,idVehiculo,Modelo_idModelo):
        sql = "INSERT INTO vehiculo VALUES (%s,%s)"
        self.db.cursor.execute(sql,(idVehiculo,Tipo_Vehiculo,Modelo_idModelo))
        self.db.commit()
          

    def update(self, Nombre_Marca,idMarca):
         sql = "UPDATE vehiculo SET Tipo_Vehiculo = %s WHERE idVehiculo = %s"
         self.db.cursor.execute(sql, (Nombre_Marca,idMarca))
         self.db.commit()

    def delete(self, idMarca):
         sql = "DELETE FROM vehiculo WHERE idVehiculo = %s"
         self.db.cursor.execute(sql, (idMarca,))
         self.db.commit()
