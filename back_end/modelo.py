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
    def generate_pdf(self):
        sql = "SELECT * FROM modelo ORDER BY Nombre_Modelo "
        self.db.cursor.execute(sql)
        resultados = self.db.cursor.fetchall()
        pdf_filename = "registro_todos_los_modelos.pdf"

        # Crear el documento PDF
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        y = 750  # Posición inicial en el eje Y

        # Títulos de las columnas
        c.drawString(100, y, "ID")
        c.drawString(200, y, "Nombre Modelo")
        c.drawString(350, y, "Año")
        c.drawString(450, y, "Marca ID")
        y -= 20  # Espacio después del encabezado

        for registro in resultados:
            c.drawString(100, y, str(registro[0]))
            c.drawString(200, y, str(registro[1]))
            c.drawString(350, y, str(registro[2]))
            c.drawString(450, y, str(registro[3]))
            y -= 20  # Espacio entre filas

        c.save()
        print(f"Se ha generado el archivo PDF: {pdf_filename}")
        
