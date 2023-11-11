import mysql.connector
class Componentes:
    def __init__(self, db):
        self.db = db

    def insert(self, Nombre_Componente,idComponente,Vehiculo_idVehiculo,Vehiculo_Modelo_idModelo):
        sql = "INSERT INTO componentes VALUES (%s,%s,%s,%s)"
        self.db.cursor.execute(sql, (Nombre_Componente,idComponente,Vehiculo_idVehiculo,Vehiculo_Modelo_idModelo))
        self.db.commit()

    def update(self, idComponente, nombre_componente):
        sql = "UPDATE componentes SET nombre_componente  = %s WHERE idComponente = %s"
        self.db.cursor.execute(sql, (nombre_componente, idComponente))
        self.db.commit()

    def delete(self, idComponente):
        sql = "DELETE FROM componentes WHERE idComponente = %s"
        self.db.cursor.execute(sql, (idComponente,))
        self.db.commit()
