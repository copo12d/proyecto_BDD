import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
import io
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
class Modelo:
    def __init__(self, db):
        self.db = db

    def insert(self, idModelo,Nombre_Modelo,Marca_idMarca):
        sql = "INSERT INTO modelo VALUES (%s,%s,%s)"
        self.db.cursor.execute(sql, (idModelo,Nombre_Modelo,Marca_idMarca))
        self.db.commit()

    def update(self, Nombre_Modelo,idModelo):
        sql = "UPDATE modelo SET Nombre_Modelo = %s WHERE idModelo = %s"
        self.db.cursor.execute(sql, (Nombre_Modelo,idModelo))
        self.db.commit()

    def delete(self, idModelo):
        sql = "DELETE FROM modelo WHERE idModelo = %s"
        self.db.cursor.execute(sql, (idModelo,))
        self.db.commit()
        
    def get_all_modelos(self):
        try:
            sql = "SELECT * FROM modelo ORDER BY idModelo"
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al obtener todos los modelos: {e}")
            return None
    
    
    def get_all_modelo_names(self):
        try:
            sql = "SELECT Nombre_Modelo FROM modelo ORDER BY Nombre_Modelo"
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            # Extraer los nombres de los resultados y devolverlos como una lista
            return [row[0] for row in result]
        except Exception as e:
            print(f"Error al obtener todos los modelos: {e}")
            return None
        
    def get_componentes_by_modelo(self, nombre_modelo):
        try:
            sql = "SELECT co.Nombre_Componente FROM componentes co JOIN vehiculo ve ON co.Vehiculo_idVehiculo = ve.idVehiculo JOIN modelo mo ON ve.Modelo_idModelo = mo.idModelo WHERE mo.Nombre_Modelo = %s"
            self.db.cursor.execute(sql, (nombre_modelo,))
            result = self.db.cursor.fetchall()
            return [row[0] for row in result]
        except Exception as e:
            print(f"Error al obtener componentes por modelo: {e}")
            return None
            
    def generate_modelos_pdf(self):
        sql = "SELECT Nombre_Modelo FROM modelo"
        self.db.cursor.execute(sql)
        resultados = self.db.cursor.fetchall()
        pdf_filename = "modelos.pdf"

        buffer = io.BytesIO()
        elements = []
        styles = getSampleStyleSheet()
        style_heading = styles['Heading1']
        style_normal = styles['Normal']

        elements.append(Paragraph("Registro de Modelos", style_heading))

        data = [["Nombre del modelo"]]
        for registro in resultados:
            nombre_modelo = str(registro[0])
            data.append([nombre_modelo])

        # Creamos la tabla
        tabla = Table(data, colWidths=[300])  # Ancho de la columna ajustado
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