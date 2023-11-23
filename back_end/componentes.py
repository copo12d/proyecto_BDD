import mysql.connector
class Componentes:
    def __init__(self, db):
        self.db = db

    def insert(self, id_Componente,Nombre_Componente,Vehiculo_idVehiculo):
        sql = "INSERT INTO componentes VALUES (%s,%s,%s)"
        self.db.cursor.execute(sql, (id_Componente,Nombre_Componente,Vehiculo_idVehiculo))
        self.db.commit()

    def update(self, id_Componente, nombre_componente):
        sql = "UPDATE componentes SET nombre_componente  = %s WHERE id_Componentes = %s"
        self.db.cursor.execute(sql, (nombre_componente, id_Componente))
        self.db.commit()

    def delete(self, id_Componente):
        sql = "DELETE FROM componentes WHERE id_Componentes = %s"
        self.db.cursor.execute(sql, (id_Componente,))
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
    
    
    def get_all_componente_names(self):
        try:
            sql = "SELECT Nombre_Componente FROM componentes ORDER BY Nombre_Componente"
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            # Extraer los nombres de los resultados y devolverlos como una lista
            return [row[0] for row in result]
        except Exception as e:
            print(f"Error al obtener todos los componentes: {e}")
            return None
