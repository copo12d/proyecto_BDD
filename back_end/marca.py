import mysql.connector
class Marca:
    def __init__(self, db):
        self.db = db

    def insert(self,idMarca,Nombre_Marca):
        sql = "INSERT INTO marca VALUES (%s,%s)"
        self.db.cursor.execute(sql,(idMarca,Nombre_Marca))
        self.db.commit()
          

    def update(self, Nombre_Marca,idMarca):
        sql = "UPDATE marca SET Nombre_Marca = %s WHERE idMarca = %s"
        self.db.cursor.execute(sql, (Nombre_Marca, idMarca))
        self.db.commit()

    def delete(self, idMarca):
         sql = "DELETE FROM marca WHERE idMarca = %s"
         self.db.cursor.execute(sql, (idMarca,))
         self.db.commit()
         
         
    def get_all_marca(self):
        try:
            sql = "SELECT * FROM marca ORDER BY idMarca"
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al obtener todos los modelos: {e}")
            return None
        
        
    def get_all_marca_names(self):
        try:
            sql = "SELECT Nombre_Marca FROM marca ORDER BY Nombre_Marca"
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            # Extraer los nombres de las tuplas y devolverlos como una lista
            return [row[0] for row in result]
        except Exception as e:
            print(f"Error al obtener todos los modelos: {e}")
            return None
