import mysql.connector
class Componentes:
    def __init__(self, db):
        self.db = db

    def insert(self, idComponente,Nombre_Componente,Vehiculo_idVehiculo):
        sql = "INSERT INTO componentes VALUES (%s,%s,%s)"
        self.db.cursor.execute(sql, (idComponente,Nombre_Componente,Vehiculo_idVehiculo))
        self.db.commit()

    def update(self, idComponente, nombre_componente):
        sql = "UPDATE componentes SET nombre_componente  = %s WHERE idComponente = %s"
        self.db.cursor.execute(sql, (nombre_componente, idComponente))
        self.db.commit()

    def delete(self, idComponente):
        sql = "DELETE FROM componentes WHERE idComponente = %s"
        self.db.cursor.execute(sql, (idComponente,))
        self.db.commit()

    def get_all_componentes(self):
        try:
            sql = "SELECT * FROM componentes ORDER BY Nombre_Componente"
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al obtener todos los modelos: {e}")
            return None
