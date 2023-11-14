import mysql.connector
class Marca:
    def __init__(self, db):
        self.db = db

    def insert(self,nombre_marca,idMarca):
        sql = "INSERT INTO marca VALUES (%s,%s)"
        self.db.cursor.execute(sql,(idMarca,nombre_marca))
        self.db.commit()
          

    def update(self, Nombre_Marca,idMarca):
         sql = "UPDATE marca SET Nombre_Marca = %s WHERE idMarca = %s"
         self.db.cursor.execute(sql, (Nombre_Marca,idMarca))
         self.db.commit()

    def delete(self, idMarca):
         sql = "DELETE FROM marca WHERE idMarca = %s"
         self.db.cursor.execute(sql, (idMarca,))
         self.db.commit()
         
         
    def get_all_marca(self):
        try:
            sql = "SELECT * FROM marca"
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al obtener todos los modelos: {e}")
            return None