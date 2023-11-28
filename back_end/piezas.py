import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
import io
from reportlab.lib.pagesizes import landscape, A3
from tkinter import messagebox

class Piezas:
    def __init__(self, db):
        self.db = db

    def insert(self, id_piezas,nombre_pieza,Estado,Peso,Medidas,id_Componentes):
        try:
            sql = "INSERT INTO piezas VALUES (%s,%s,%s,%s,%s,%s)"
            self.db.cursor.execute(sql, (id_piezas,nombre_pieza,Estado,Peso,Medidas,id_Componentes))
            self.db.commit()
        except mysql.connector.Error as ex:
            print(f"fallo la conecxion {ex}")

    def update(self, id_Piezas, Nombre_Pieza,Estado,Peso,Medidas):
        try:
            sql = """UPDATE piezas SET nombre_pieza = %s,Estado = %s, Peso = %s, Medidas = %s 
            WHERE id_piezas = %s"""
            self.db.cursor.execute(sql, (id_Piezas,Nombre_Pieza,Estado,Peso,Medidas))
            self.db.commit()
        except mysql.connector.Error as ex:
            print(f"fallo la conecxion {ex}")
            
    def delete(self, id_Piezas):
        try:
            sql = "DELETE FROM piezas WHERE id_piezas = %s"
            self.db.cursor.execute(sql, (id_Piezas,))
            self.db.commit()
        except mysql.connector.Error as ex:
            print(f"fallo la conecxion {ex}")

    def get_all_piezas(self):
        try:
            sql = "SELECT * FROM piezas ORDER BY id_piezas"
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al obtener todas las piezas: {e}")
            return None
        
    def get_piezas_with_details(self, nombre_marca, nombre_modelo, nombre_componente):
        try:
            sql = """
                SELECT  pi.nombre_pieza,pi.Estado,pi.Peso,pi.Medidas, ve.año
                FROM modelo mo
                JOIN marca ma ON mo.Marca_idMarca = ma.idMarca
                JOIN vehiculo ve ON ve.Modelo_idModelo = mo.idModelo
                JOIN componentes co ON co.Vehiculo_idVehiculo = ve.idVehiculo
                JOIN piezas pi ON pi.id_Componente = co.id_Componentes
                WHERE ma.nombre_marca = %s
                AND mo.Nombre_Modelo = %s
                AND co.Nombre_Componente = %s;
            """
            self.db.cursor.execute(sql, (nombre_marca, nombre_modelo, nombre_componente))
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al obtener las piezas: {e}")
            return None
            
    def generate_pdf(self):
        sql = """SELECT ma.Nombre_marca, mo.Nombre_Modelo, co.Nombre_Componente, ve.Tipo_Vehiculo, pi.nombre_pieza, ve.año
                FROM modelo mo
                JOIN marca ma ON mo.Marca_idMarca = ma.idMarca
                JOIN componentes co ON co.Vehiculo_idVehiculo = ma.idMarca
                JOIN piezas pi ON pi.id_Componente = co.id_Componentes
                JOIN vehiculo ve ON ve.Modelo_idModelo = mo.idModelo;
                """
        self.db.cursor.execute(sql)
        resultados = self.db.cursor.fetchall()
        pdf_filename = "piezas.pdf"

        buffer = io.BytesIO()
        elements = []
        styles = getSampleStyleSheet()
        style_heading = styles['Heading1']
        style_normal = styles['Normal']

        elements.append(Paragraph("Registro de Piezas ", style_heading))

        data = [["Nombre de la marca", "Nombre del modelo", "Nombre del componente", "Tipo de vehículo", "Nombre de la pieza", "Año"]]
        for registro in resultados:
            nombre_marca = str(registro[0])
            nombre_modelo = str(registro[1])
            nombre_componente = str(registro[2])
            tipo_carro = str(registro[3])
            nombre_pieza = str(registro[4])
            año = str(registro[5])
            data.append([nombre_marca, nombre_modelo, nombre_componente, tipo_carro, nombre_pieza, año])

        # Creamos la tabla
        tabla = Table(data, colWidths=[100, 120, 120, 80, 150, 50])  # Ajuste de los anchos de las columnas
        tabla.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

        elements.append(tabla)
        pdf = SimpleDocTemplate(buffer, pagesize=landscape(A3))
        pdf.build(elements)

        with open(pdf_filename, "wb") as f:
            f.write(buffer.getvalue())

        mensajito=messagebox.showinfo("SIUUUU",f"Se ha generado el archivo PDF: {pdf_filename}")