import mysql.connector
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
import io

class Piezas:
    def __init__(self, db):
        self.db = db

    def insert(self, id_piezas,nombre_pieza,descripcion,id_Componentes):
        try:
            sql = "INSERT INTO piezas VALUES (%s,%s,%s,%s)"
            self.db.cursor.execute(sql, (id_piezas,nombre_pieza,descripcion,id_Componentes))
            self.db.commit()
        except mysql.connector.Error as ex:
            print(f"fallo la conecxion {ex}")

    def update(self, id_Piezas, Nombre_Pieza,descripcion):
        try:
            sql = "UPDATE piezas SET Nombre_Pieza = %s, descripcion = %s WHERE id_Pieza = %s"
            self.db.cursor.execute(sql, (id_Piezas,Nombre_Pieza,descripcion ))
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
            
    def get_all_piezass(self, nombre_marca, nombre_modelo, nombre_componente):
        try:
            sql = """SELECT mo.Nombre_Modelo, ma.nombre_marca, pi.nombre_pieza
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
        except mysql.connector.Error as e:
            print(f"Error al obtener todas las piezas: {e}")

            
    def generate_pdf(self, nombre):
        sql = """SELECT mo.Nombre_Modelo, co.Nombre_Componente, pi.nombre_pieza
                FROM modelo mo
                JOIN marca ma ON mo.Marca_idMarca = ma.idMarca
                JOIN componentes co ON co.Vehiculo_idVehiculo = ma.idMarca
                JOIN piezas pi ON pi.id_Componente = co.id_Componentes;
                """
        self.db.cursor.execute(sql)
        resultados = self.db.cursor.fetchall()
        pdf_filename = nombre + ".pdf"

        buffer = io.BytesIO()
        elements = []
        styles = getSampleStyleSheet()
        style_heading = styles['Heading1']
        style_normal = styles['Normal']

        elements.append(Paragraph("Registro de Piezas", style_heading))

        data = [["Nombre del modelo", "Nombre del componente", "Nombre de la pieza"]]
        for registro in resultados:
            nombre_modelo = str(registro[0])
            nombre_componente = str(registro[1])
            nombre_pieza = str(registro[2])
            data.append([nombre_modelo, nombre_componente, nombre_pieza])

        # Creamos la tabla
        tabla = Table(data, colWidths=[150, 150, 150])
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

        print(f"Se ha generado el archivo PDF: {pdf_filename}")
        
    
            
    