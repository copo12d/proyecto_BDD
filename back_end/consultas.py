import tkinter as tk
from tkinter import ttk
from back_end import Database  # Importa tu módulo de conexión a la base de datos
from piezas import Piezas
from marca import Marca
from modelo import Modelo
from vehiculo import Vehiculo
from componentes import Componentes
from tkinter import *

class MyApp:
    def __init__(self, root):
        
        self.db = Database(user='root', password='0704', host='127.0.0.1', database='proyecto2')  # Reemplaza con tus credenciales
        self.marca = Marca(self.db)
        self.pieza = Piezas(self.db)
        self.modelo = Modelo(self.db)
        self.vehiculo = Vehiculo(self.db)
        self.componente = Componentes(self.db)

        self.espacio=tk.Label(root, text="  ").grid(row=1,column=0)
        
        self.marca_combobox = ttk.Combobox(root, state="readonly", width=30)
        self.marca_combobox.grid(row=2,column=0)

        self.modelo_combobox = ttk.Combobox(root, state="readonly",width=30)
        self.modelo_combobox.grid(row=3,column=0)
        self.labeleliges=Label(root,text="SELECCIONA  ", fg="#000000", font=('crushed', 16, 'bold')).grid(row=0,column=0, columnspan=5)
        self.componente_combobox = ttk.Combobox(root, state="readonly",width=30)
        self.componente_combobox.grid(row=4,column=0)

        self.espacio2=tk.Label(root, text=" \n ").grid(row=5,column=0)

        self.tabla=ttk.Treeview(root, columns=(1,2,3,4,5), show="headings")
        self.tabla.grid(row=6,column=0)
        self.mostrar_resultados(None)

        self.scroll=ttk.Scrollbar(root, orient=VERTICAL, command= self.tabla.yview)
        self.scroll.grid(row=6, column=3, sticky=NSEW)
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.cargar_marcas()
        self.marca_combobox.bind("<<ComboboxSelected>>", self.cargar_modelos)
        self.modelo_combobox.bind("<<ComboboxSelected>>", self.cargar_componentes)
        self.componente_combobox.bind("<<ComboboxSelected>>", self.mostrar_resultados)

    def cargar_marcas(self):
        marcas = self.marca.get_all_marca_names()
        if marcas:
            self.marca_combobox['values'] = marcas
            #self.marca_combobox.current(0)  # Seleccionar el primer elemento por defecto

    def cargar_modelos(self, event):
        marca_seleccionada = self.marca_combobox.get()
        modelos = self.marca.get_modelos_by_marca(marca_seleccionada)
        if modelos:
            self.modelo_combobox['values'] = modelos
            self.modelo_combobox.current(0)  # Seleccionar el primer elemento por defecto

    def cargar_componentes(self, event):
        modelo_seleccionado = self.modelo_combobox.get()
        componentes = self.modelo.get_componentes_by_modelo(modelo_seleccionado)
        if componentes:
            self.componente_combobox['values'] = componentes
            self.componente_combobox.current(0)  # Seleccionar el primer elemento por defecto

    def mostrar_resultados(self, event):
        
        componente_seleccionado = self.componente_combobox.get()
        marca_seleccionada = self.marca_combobox.get()
        modelo_seleccionado = self.modelo_combobox.get()
        
                        
        
        

        self.tabla.heading(1, text="nombre_pieza")
        self.tabla.heading(2, text="Estado")
        self.tabla.heading(3, text="Peso")
        self.tabla.heading(4, text="Medidas")
        self.tabla.heading(5, text="Año")

        self.tabla.column(1,width=180)
        self.tabla.column(2,width=180)
        self.tabla.column(3,width=180)
        self.tabla.column(4,width=180)
        self.tabla.column(5,width=180)
                        
                            
                            
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        registros=self.pieza.get_piezas_with_details(marca_seleccionada, modelo_seleccionado,componente_seleccionado)

        for registro in registros:
            self.tabla.insert("", "end", values=registro)


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    
    root.mainloop()
