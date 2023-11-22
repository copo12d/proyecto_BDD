import mysql.connector
from back_end import Database
from piezas import Piezas
from marca import Marca
from modelo import Modelo
from vehiculo import Vehiculo
from componentes import Componentes
import tkinter as tk
from tkinter import ttk

def main():
    
    db = Database("127.0.0.1","root","30412187","mydb")
    marca = Marca(db)
    pieza = Piezas(db)
    modelo = Modelo(db)
    vehiculo = Vehiculo(db)
    componentes = Componentes(db)
    
    try:
        if db:
            root = tk.Tk()
            root.title("Ejemplo Combobox")

# Crear la función para obtener las marcas
        def cargar_marcas():
            marcas = marca.get_all_marca_names()
            print(marcas)
            if marcas:
                combobox['values'] = marcas
                combobox.current(0)  # Seleccionar el primer elemento por defecto
            else:
                combobox['values'] = ['Error al cargar las marcas']

        # Crear el Combobox
        combobox = ttk.Combobox(root, state="readonly")
        combobox.pack(padx=20, pady=10)

        # Botón para cargar las marcas
        btn_cargar = tk.Button(root, text="Cargar Marcas", command=cargar_marcas)
        btn_cargar.pack(pady=5)

        root.mainloop()
            
            
            
            
            
            
            
            
            
       
    except mysql.connector.Error as e:
        print(f"hubo un error en la coneccion{e}")
    
    finally:  
        if db:
            db.close_connection()
            print("finalizo la conexion")
    

if __name__=="__main__":
    main()
    
    