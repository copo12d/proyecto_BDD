import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
import io
from tkinter import messagebox
class Componentes:
    def __init__(self, db):
        self.db = db

    def insert(self, id_Componentes,Nombre_Componente,Vehiculo_idVehiculo):
        sql = "INSERT INTO componentes VALUES (%s,%s,%s)"
        self.db.cursor.execute(sql, (id_Componentes,Nombre_Componente,Vehiculo_idVehiculo))
        self.db.commit()

    def update(self, nombre_componente,id_Componentes):
        sql = "UPDATE componentes SET nombre_componente  = %s WHERE id_Componentes = %s"
        self.db.cursor.execute(sql, (nombre_componente, id_Componentes))
        self.db.commit()

    def delete(self, id_Componente):
        sql = "DELETE FROM componentes WHERE id_Componentes = %s"
        self.db.cursor.execute(sql, (id_Componente,))
        self.db.commit()

    def get_all_componentes(self):
        try:
            sql = "SELECT * FROM componentes ORDER BY id_Componentes"
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
        
    def get_piezas_by_componente(self, nombre_componente):
        try:
            sql = "SELECT pi.nombre_pieza FROM piezas pi JOIN componentes co ON pi.id_Componente = co.id_Componentes WHERE co.Nombre_Componente = %s"
            self.db.cursor.execute(sql, (nombre_componente,))
            result = self.db.cursor.fetchall()
            return [row[0] for row in result]
        except Exception as e:
            print(f"Error al obtener piezas por componente: {e}")
            return None

    def generate_componentes_pdf(self):
        sql = """SELECT co.Nombre_Componente, ve.Tipo_Vehiculo
                FROM componentes co
                LEFT JOIN vehiculo ve ON co.Vehiculo_idVehiculo = ve.idVehiculo"""
        self.db.cursor.execute(sql)
        resultados = self.db.cursor.fetchall()
        pdf_filename = "componentes.pdf"

        buffer = io.BytesIO()
        elements = []
        styles = getSampleStyleSheet()
        style_heading = styles['Heading1']
        style_normal = styles['Normal']

        elements.append(Paragraph("Registro de Componentes con Vehículos", style_heading))

        data = [["Nombre del componente", "Tipo de vehículo"]]
        for registro in resultados:
            nombre_componente = str(registro[0])
            tipo_vehiculo = str(registro[1])
            data.append([nombre_componente, tipo_vehiculo])

        # Creamos la tabla
        tabla = Table(data, colWidths=[200, 200])  # Ajusta el ancho de las columnas según sea necesario
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