import tkinter as tk
from tkinter import ttk
from back_end import Database  # Importa tu módulo de conexión a la base de datos
from piezas import Piezas
from marca import Marca
from modelo import Modelo
from vehiculo import Vehiculo
from componentes import Componentes

class MyApp:
    def __init__(self, root):
        self.db = Database(user='root', password='0704', host='127.0.0.1', database='proyecto2')  # Reemplaza con tus credenciales
        self.marca = Marca(self.db)
        self.pieza = Piezas(self.db)
        self.modelo = Modelo(self.db)
        self.vehiculo = Vehiculo(self.db)
        self.componente = Componentes(self.db)

        self.espacio=tk.Label(root, text="  ").grid(row=0,column=0)

        self.marca_combobox = ttk.Combobox(root, state="readonly")
        self.marca_combobox.grid(row=1,column=0)

        self.modelo_combobox = ttk.Combobox(root, state="readonly")
        self.modelo_combobox.grid(row=2,column=0)

        self.componente_combobox = ttk.Combobox(root, state="readonly")
        self.componente_combobox.grid(row=3,column=0)

        self.espacio2=tk.Label(root, text=" \n ").grid(row=4,column=0)

        #self.resultados_text = tk.Text(root, height=10, width=50)
        #self.resultados_text.grid(row=5,column=0)

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
            self.modelo_combobox.current(0) # Seleccionar el primer elemento por defecto

    def cargar_componentes(self, event):
        modelo_seleccionado = self.modelo_combobox.get()
        componentes = self.modelo.get_componentes_by_modelo(modelo_seleccionado)
        if componentes:
            self.componente_combobox['values'] = componentes
            self.componente_combobox.current(0)  # Seleccionar el primer elemento por defecto

    def mostrar_resultados(self, event):
        marca_seleccionada = self.marca_combobox.get()
        modelo_seleccionado = self.modelo_combobox.get()
        componente_seleccionado = self.componente_combobox.get()

        # Aquí deberías ejecutar la consulta con los parámetros seleccionados
        resultados = self.pieza.get_all_piezass(marca_seleccionada, modelo_seleccionado, componente_seleccionado)
        self.resultados_text.delete('1.0', tk.END)  # Limpiar el Text
        if resultados:
            for resultado in resultados:
                self.resultados_text.insert(tk.END, f"{resultado}\n")
        else:
            self.resultados_text.insert(tk.END, "No se encontraron resultados.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
