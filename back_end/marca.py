import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
import io
from tkinter import messagebox
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
        
    def get_modelos_by_marca(self, nombre_marca):
        try:
            sql = "SELECT mo.Nombre_Modelo FROM modelo mo JOIN marca ma ON mo.Marca_idMarca = ma.idMarca WHERE ma.Nombre_Marca = %s"
            self.db.cursor.execute(sql, (nombre_marca,))
            result = self.db.cursor.fetchall()
            return [row[0] for row in result]
        except Exception as e:
            print(f"Error al obtener modelos por marca: {e}")
            return None

    def generate_marcas_pdf(self):
        sql = "SELECT Nombre_marca FROM marca;"
        self.db.cursor.execute(sql)
        resultados = self.db.cursor.fetchall()
        pdf_filename = "marcas.pdf"

        buffer = io.BytesIO()
        elements = []
        styles = getSampleStyleSheet()
        style_heading = styles['Heading1']
        style_normal = styles['Normal']

        elements.append(Paragraph("Registro de Marcas", style_heading))

        data = [["Nombre de la marca"]]
        for registro in resultados:
            nombre_marca = str(registro[0])
            data.append([nombre_marca])

        # Creamos la tabla
        tabla = Table(data, colWidths=[200])
        tabla.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

        elements.append(tabla)
        pdf = SimpleDocTemplate(buffer, pagesize=letter)
        pdf.build(elements)

        with open(pdf_filename, "wb") as f:
            f.write(buffer.getvalue())

        mensajito=messagebox.showinfo("SIUUUU",f"Se ha generado el archivo PDF: {pdf_filename}")