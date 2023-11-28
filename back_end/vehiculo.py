import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
import io
from tkinter import messagebox
class Vehiculo:
    def __init__(self, db):
        self.db = db

    def insert(self,idVehiculo,Tipo_Vehiculo,Modelo_idModelo,año):
        sql = "INSERT INTO vehiculo VALUES (%s,%s,%s,%s)"
        self.db.cursor.execute(sql,(idVehiculo,Tipo_Vehiculo,Modelo_idModelo,año))
        self.db.commit()
          

    def update(self, idVehiculo, tipo_vehiculo, idModelo, año):
        try:
            sql = "UPDATE vehiculo SET Tipo_Vehiculo = %s, Modelo_idModelo = %s, año = %s WHERE idVehiculo = %s"
            values = (tipo_vehiculo, idModelo, año, idVehiculo)
            self.db.cursor.execute(sql, values)
            self.db.commit()
            print("Vehículo actualizado correctamente.")
        except mysql.connector.Error as e:
            print(f"Error al actualizar el vehículo: {e}")

    def delete(self, idVehiculo):
         sql = "DELETE FROM vehiculo WHERE idVehiculo = %s"
         self.db.cursor.execute(sql, (idVehiculo,))
         self.db.commit()
    
    def get_all_Vehiculos(self):
        try:
            sql = "SELECT * FROM Vehiculo ORDER BY idVehiculo"
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al obtener todos los modelos: {e}")
            return None

    def generate_vehiculo_pdf(self):
        sql = "SELECT Tipo_Vehiculo, año FROM vehiculo;"
        self.db.cursor.execute(sql)
        resultados = self.db.cursor.fetchall()
        pdf_filename = "vehiculos.pdf"

        buffer = io.BytesIO()
        elements = []
        styles = getSampleStyleSheet()
        style_heading = styles['Heading1']
        style_normal = styles['Normal']

        elements.append(Paragraph("Registro de Vehículos", style_heading))

        data = [["Tipo de vehículo", "Año"]]
        for registro in resultados:
            tipo_vehiculo = str(registro[0])
            año = str(registro[1])
            data.append([tipo_vehiculo, año])

        # Creamos la tabla
        tabla = Table(data, colWidths=[200, 50])
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