import mysql.connector
from back_end import Database
from piezas import Piezas
from marca import Marca
from modelo import Modelo
from vehiculo import Vehiculo
from componentes import Componentes
from consultas import MyApp
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import re



def main():
    
    db = Database("127.0.0.1","root","0704","proyecto2")
    marca = Marca(db)
    pieza = Piezas(db)
    modelo = Modelo(db)
    vehiculo = Vehiculo(db)
    componentes = Componentes(db)



    try:
        if db:



        #---------DEFINIENDO LA RAIZ Y LA IMAGEN DEL INICIO---------


            root=Tk()

            root.resizable(height=FALSE, width=FALSE)
            root.title("Grupo VAS System")
            root.iconbitmap("logo.ico")
            image4=ImageTk.PhotoImage(Image.open("menu.jpg"))
            label_inicio=Label(root, image=image4)
            label_inicio.pack()
            ancho=image4.width()
            alto=image4.height()
            root.geometry(f"{ancho}x{alto}+100+100")


        
            #---------DEFINIENDO EL INICIO Y LA FUNCION PARA MOSTRAR LOS FRAMES (Y ELIMINAR LA IMAGEN DE INICIO)---------

            def mostrarframe(frame):
                
                for f in frames:
                    f.pack_forget()
                

                if frame==consultassframe:
                    consultasframebtn()
                    
                    

                frame.pack(expand=False)
                label_inicio.pack_forget()
                
                
                if frame==vehiculoframe or frame==componentesframe or frame==piezasframe or frame==marcaframe or frame==modeloframe:
                    
                    widgetstablas(frame)
                    
                    
                    



            def iniciobtn():
                
                for f in frames:
                    f.pack_forget()

                label_inicio.pack()

            def consultasframebtn():
                
                for f in frames:
                    f.pack_forget()
                MyApp(consultassframe)

            def ayudam():
                mensajito=messagebox.showinfo("Ayuda", "1. Para agregar un nuevo registro, Presione \"Nuevo\" y cuando haya completado todos los campos, presione \"Agregar\" \n\n2. Para editar un registro, seleccione el registro que desea editar, cambie los datos en los campos de texto, y pulse \"Guardar\"\n\n3. Para eliminar un registro, seleccione el registro a eliminar, y pulse \"Eliminar\". Tenga en cuenta la advertencia de las 'Parent Rows'")

            
            
                       


            #-------------FUNCIONES DE LOS BOTONES DEl MENU------------

           

            def tablacomponentes():
                mostrarframe(componentesframe)
                    
            def tablavehiculo():
                mostrarframe(vehiculoframe)

            def tablamarca():
                mostrarframe(marcaframe)

            def tablapiezas():
                mostrarframe(piezasframe)

            def tablamodelo():
                mostrarframe(modeloframe)

            


            #---------------FUNCIONES PARA VERIFICAR SI UNA ROW ES PARENT-------------


            def Componentesesparent(id):
                # Conectarse a la base de datos
                conn = mysql.connector.connect(user='root', password='0704', host='127.0.0.1', database='proyecto')
                cursor = conn.cursor()

                # Ejecutar una consulta para verificar si hay registros relacionados
                query = f"SELECT * FROM componentes WHERE id_componentes = {id}"
                cursor.execute(query)
                registros_relacionados = cursor.fetchall()

                # Cerrar la conexión
                cursor.close()
                conn.close()

                # Devolver True si hay registros relacionados, lo que significa que es una parent row
                return len(registros_relacionados) > 0
            


            def Vehiculoesparent(id):
                # Conectarse a la base de datos
                conn = mysql.connector.connect(user='root', password='0704', host='127.0.0.1', database='proyecto')                
                cursor = conn.cursor()

                # Ejecutar una consulta para verificar si hay registros relacionados
                query = f"SELECT * FROM componentes WHERE Vehiculo_idVehiculo = {id}"
                cursor.execute(query)
                registros_relacionados = cursor.fetchall()

                # Cerrar la conexión
                cursor.close()
                conn.close()

                # Devolver True si hay registros relacionados, lo que significa que es una parent row
                return len(registros_relacionados) > 0
            


            def Modeloesparent(id):
                # Conectarse a la base de datos
                conn = mysql.connector.connect(user='root', password='0704', host='127.0.0.1', database='proyecto')
                cursor = conn.cursor()

                # Ejecutar una consulta para verificar si hay registros relacionados
                query = f"SELECT * FROM vehiculo WHERE Modelo_idModelo = {id}"
                cursor.execute(query)
                registros_relacionados = cursor.fetchall()

                # Cerrar la conexión
                cursor.close()
                conn.close()

                # Devolver True si hay registros relacionados, lo que significa que es una parent row
                return len(registros_relacionados) > 0
            


            def Marcaesparent(id):
                # Conectarse a la base de datos
                conn = mysql.connector.connect(user='root', password='0704', host='127.0.0.1', database='proyecto')
                cursor = conn.cursor()

                # Ejecutar una consulta para verificar si hay registros relacionados
                query = f"SELECT * FROM modelo WHERE Marca_idMarca = {id}"
                cursor.execute(query)
                registros_relacionados = cursor.fetchall()

                # Cerrar la conexión
                cursor.close()
                conn.close()

                # Devolver True si hay registros relacionados, lo que significa que es una parent row
                return len(registros_relacionados) > 0
            
            
            
           
                




            


            


             #---------WIDGETS DE LOS FRAMES DE LAS TABLAS---------




         #-----------------WIDGETS DE LAS TABLAS-------------------

            def widgetstablas(frame):
                
                if frame==modeloframe:
                    
                    def agregarbtn():
                        
                        modelo.insert(int(idModeloentry.get()),Nombre_Modeloentry.get(),int(idMarcaentry.get()))

                        idModeloentry.delete(0,END)
                        Nombre_Modeloentry.delete(0,END)
                        idMarcaentry.delete(0,END)
                        
                        tablac()
                        
                    def actualizar():
                        global tabla
                        Guardar.config(state=NORMAL)
                        modelo.update(Nombre_Modeloentry.get(),int(idModeloentry.get()))
                        Nuevo.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        tablac()
                        

                    def editarbtn():
                        global tabla
                        idModeloentry.config(state=NORMAL)
                        idMarcaentry.config(state=NORMAL)
                        Guardar.config(state=NORMAL)
                        idModeloentry.delete(0,END)
                        Nombre_Modeloentry.delete(0,END)
                        idMarcaentry.delete(0,END)
                        

                        idModelovalor=tabla.item(tabla.selection())['values'][0]
                        Nombre_Modelovalor=tabla.item(tabla.selection())['values'][1]
                        idMarcavalor=tabla.item(tabla.selection())['values'][2]


                        idModeloentry.insert(0,idModelovalor)
                        Nombre_Modeloentry.insert(0,Nombre_Modelovalor)
                        idMarcaentry.insert(0,idMarcavalor)
                        idModeloentry.config(state=DISABLED)
                        idMarcaentry.config(state=DISABLED)
                        
                        Nuevo.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        
                     
                    def borrarbtn():
                        global tabla
                        id_modelo=tabla.item(tabla.selection())['values'][0]
                        if Modeloesparent(id_modelo):
                            mensaje=messagebox.askyesno("Advertencia", "¿Estás seguro de que quieres eliminar este registro? Es un Parent Row, por lo que se eliminarán todos los Child Rows de otras tablas.")
                            if mensaje:
                                modelo.delete(id_modelo)
                                Nuevo.config(state=NORMAL)
                                tablac()
                            else:
                                tablac()
                        else:
                            modelo.delete(id_modelo)
                            Nuevo.config(state=NORMAL)
                            tablac()

                           

                    def guardarbtn():
                        idModeloentry.config(state=NORMAL)
                        idMarcaentry.config(state=NORMAL)
                        actualizar()
                        idModeloentry.delete(0,END)
                        Nombre_Modeloentry.delete(0,END)
                        idMarcaentry.delete(0,END)
                        Guardar.config(state=DISABLED)
                        Nuevo.config(state=NORMAL)
                        Editar.config(state=DISABLED)
                        Eliminar.config(state=DISABLED)
                        
                    
                    registros=modelo.get_all_modelos()



                    def nuevobtn():
                        global tabla
                        idModeloentry.delete(0,END)
                        Nombre_Modeloentry.delete(0,END)
                        idMarcaentry.delete(0,END)
                        

                        tabla.selection_remove(tabla.selection())
                        Editar.config(state=DISABLED)
                        Eliminar.config(state=DISABLED)
                        Agregar.config(state=NORMAL)


                    
                    def elementos(event=NONE):
                        global tabla
                        if tabla.selection():
                            Editar.config(state=NORMAL)
                            Eliminar.config(state=NORMAL)

                    

                    def cancelarbtn():
                        global tabla
                        idModeloentry.config(state=NORMAL)
                        idMarcaentry.config(state=NORMAL)
                        idModeloentry.delete(0,END)
                        Nombre_Modeloentry.delete(0,END)
                        idMarcaentry.delete(0,END)
                        

                        tabla.selection_remove(tabla.selection())
                        Editar.config(state=DISABLED)
                        Eliminar.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        Nuevo.config(state=NORMAL)
                        
                            




                    idModeloentry=Entry(modeloframe, width=30)
                    Nombre_Modeloentry=Entry(modeloframe, width=30)
                    idMarcaentry=Entry(modeloframe, width=30)
                    

                    
                    
                    idModeloentry.grid(row=0,column=1)
                    Nombre_Modeloentry.grid(row=1,column=1)
                    idMarcaentry.grid(row=2,column=1)
                    

                        
                    

                    idModelolabel=Label(modeloframe,text="idModelo (P)", fg="#000000", font=('crushed', 12, 'bold')).grid(row=0,column=0)
                    Nombre_Modelolabel=Label(modeloframe,text="Nombre_Modelo", fg="#000000", font=('crushed', 12, 'bold')).grid(row=1,column=0)
                    idMarcalabel=Label(modeloframe,text="idMarca (F)", fg="#000000", font=('crushed', 12, 'bold')).grid(row=2,column=0)
                    
                    
                    ayudabtn=Button(modeloframe,text="?", padx=12,pady=1.5, command=ayudam, bg="#41c0b8", font=('crushed', 10))
                    ayudabtn.grid(row=1,column=2)   
                    Nuevo=Button(modeloframe, text="Nuevo", command=nuevobtn, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Nuevo.grid(row=4,column=0)
                    Agregar=Button(modeloframe, text="Agregar", command=agregarbtn, state=DISABLED,padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Agregar.grid(row=4, column=1)
                    Cancelar=Button(modeloframe, text="Cancelar", command=cancelarbtn, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Cancelar.grid(row=4,column=2)

                    Editar=Button(modeloframe, text="Editar", command=editarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Editar.grid(row=8,column=0)
                    Eliminar=Button(modeloframe, text="Eliminar", command=borrarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Eliminar.grid(row=8, column=1)
                    Guardar=Button(modeloframe, text="Guardar", command=guardarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Guardar.grid(row=8,column=2)
                    espacio2=Label(modeloframe, text="     ").grid(row=5,column=0)
                    espacio3=Label(modeloframe, text="     ").grid(row=7,column=0)

                    
                    

                    

                    
                    def tablac(): 
                        
                        global tabla

                        tabla=ttk.Treeview(modeloframe, columns=(1,2,3), show="headings")
                        
                        scroll=ttk.Scrollbar(modeloframe, orient=VERTICAL, command= tabla.yview)
                        scroll.grid(row=6, column=3, sticky=NSEW)
                        tabla.configure(yscrollcommand=scroll.set)

                        tabla.heading(1, text="idModelo")
                        tabla.heading(2, text="Nombre_Modelo")
                        tabla.heading(3, text="idMarca")
                        
                            
                            
                        for item in tabla.get_children():
                            tabla.delete(item)

                        registros=modelo.get_all_modelos()
                        
                        
                        

                        for registro in registros:
                            tabla.insert("", "end", values=registro)

                        tabla.grid(row=6,column=0,columnspan=3, sticky="nsew")
                        tabla.bind("<<TreeviewSelect>>", elementos)
                        

                    
                    tablac()
                    elementos()
                 


                elif frame==piezasframe:

                    def agregarbtn():
                        
                        pieza.insert(int(id_piezasentry.get()),nombre_piezaentry.get(),estadoentry.get(), float(pesoentry.get()), medidasentry.get(),int(id_Componenteentry.get()))
                        
                        id_piezasentry.delete(0,END)
                        nombre_piezaentry.delete(0,END)
                        estadoentry.delete(0,END)
                        pesoentry.delete(0,END)
                        medidasentry.delete(0,END)
                        id_Componenteentry.delete(0,END)
                        
                        tablac()
                        

                    def editarbtn():
                        global tabla
                        id_piezasentry.config(state=NORMAL)
                        
                        Guardar.config(state=NORMAL)
                        id_piezasentry.delete(0,END)
                        nombre_piezaentry.delete(0,END)
                        estadoentry.delete(0,END)
                        pesoentry.delete(0,END)
                        medidasentry.delete(0,END)
                        id_Componenteentry.delete(0,END)
                        

                        idpiezasvalor=tabla.item(tabla.selection())['values'][0]
                        nombrepiezavalor=tabla.item(tabla.selection())['values'][1]
                        estadovalor=tabla.item(tabla.selection())['values'][2]
                        pesovalor=tabla.item(tabla.selection())['values'][3]
                        medidasvalor=tabla.item(tabla.selection())['values'][4]
                        idcomponentevalor=tabla.item(tabla.selection())['values'][5]
                        

                        id_piezasentry.insert(0,idpiezasvalor)
                        nombre_piezaentry.insert(0,nombrepiezavalor)
                        estadoentry.insert(0,estadovalor)
                        pesoentry.insert(0,pesovalor)
                        medidasentry.insert(0,medidasvalor)
                        id_Componenteentry.insert(0,idcomponentevalor)

                        id_piezasentry.config(state=DISABLED)
                        
                        
                        Nuevo.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        
                     
                    def borrarbtn():
                        global tabla

                        idpiezas=tabla.item(tabla.selection())['values'][0]
                        
                        pieza.delete(idpiezas)
                        Nuevo.config(state=NORMAL)
                        tablac()
                           

                    def guardarbtn():
                        id_piezasentry.config(state=NORMAL)
                        borrarbtn()
                        agregarbtn()
                        

                        Guardar.config(state=NORMAL)
                        id_piezasentry.delete(0,END)
                        nombre_piezaentry.delete(0,END)
                        estadoentry.delete(0,END)
                        pesoentry.delete(0,END)
                        medidasentry.delete(0,END)
                        id_Componenteentry.delete(0,END)
                        Guardar.config(state=DISABLED)
                        Nuevo.config(state=NORMAL)
                        tabla.selection_remove(tabla.selection())
                        Editar.config(state=DISABLED)
                        Eliminar.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        
                    
                    registros=pieza.get_all_piezas()



                    def nuevobtn():
                        id_piezasentry.delete(0,END)
                        nombre_piezaentry.delete(0,END)
                        estadoentry.delete(0,END)
                        pesoentry.delete(0,END)
                        medidasentry.delete(0,END)
                        id_Componenteentry.delete(0,END)
                        
                        Agregar.config(state=NORMAL)
                    
                    def elementos(event=NONE):
                        global tabla
                        if tabla.selection():
                            Editar.config(state=NORMAL)
                            Eliminar.config(state=NORMAL)
                    

                    def cancelarbtn():
                        global tabla
                        id_piezasentry.config(state=NORMAL)
                        id_piezasentry.delete(0,END)
                        nombre_piezaentry.delete(0,END)
                        estadoentry.delete(0,END)
                        pesoentry.delete(0,END)
                        medidasentry.delete(0,END)
                        id_Componenteentry.delete(0,END)
                        

                        tabla.selection_remove(tabla.selection())
                        Editar.config(state=DISABLED)
                        Eliminar.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        Nuevo.config(state=NORMAL)
                        
                            


                    id_piezasentry=Entry(piezasframe, width=30)
                    nombre_piezaentry=Entry(piezasframe, width=30)
                    estadoentry=Entry(piezasframe, width=30)
                    pesoentry=Entry(piezasframe, width=30)
                    medidasentry=Entry(piezasframe, width=30)
                    id_Componenteentry=Entry(piezasframe, width=30)
                    
                    id_piezasentry.grid(row=0,column=1)
                    nombre_piezaentry.grid(row=1,column=1)
                    estadoentry.grid(row=2,column=1)
                    pesoentry.grid(row=3,column=1)
                    medidasentry.grid(row=4,column=1)
                    id_Componenteentry.grid(row=5,column=1)
                    
                

                    id_piezaslabel=Label(piezasframe,text="id_pieza (P)", fg="#000000", font=('crushed', 12, 'bold')).grid(row=0,column=0)
                    nombre_piezalabel=Label(piezasframe,text="nombre_pieza", fg="#000000", font=('crushed', 12, 'bold')).grid(row=1,column=0)
                    estadolabel=Label(piezasframe,text="Estado", fg="#000000", font=('crushed', 12, 'bold')).grid(row=2,column=0)
                    pesolabel=Label(piezasframe,text="Peso (g)", fg="#000000", font=('crushed', 12, 'bold')).grid(row=3,column=0)
                    medidaslabel=Label(piezasframe,text="Medidas", fg="#000000", font=('crushed', 12, 'bold')).grid(row=4,column=0)
                    id_Componentelabel=Label(piezasframe,text="idComponente (F)", fg="#000000", font=('crushed', 12, 'bold')).grid(row=5,column=0)
                    
                    
                    ayudabtn=Button(piezasframe,text="?", padx=12,pady=1.5, command=ayudam, bg="#41c0b8", font=('crushed', 10))
                    ayudabtn.grid(row=1,column=2)   
                    Nuevo=Button(piezasframe, text="Nuevo", command=nuevobtn, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Nuevo.grid(row=6,column=0)
                    Agregar=Button(piezasframe, text="Agregar", command=agregarbtn, state=DISABLED,padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Agregar.grid(row=6, column=1)
                    Cancelar=Button(piezasframe, text="Cancelar", command=cancelarbtn, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Cancelar.grid(row=6,column=2)

                    Editar=Button(piezasframe, text="Editar", command=editarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Editar.grid(row=10,column=0)
                    Eliminar=Button(piezasframe, text="Eliminar", command=borrarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Eliminar.grid(row=10, column=1)
                    Guardar=Button(piezasframe, text="Guardar", command=guardarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Guardar.grid(row=10,column=2)
                    espacio2=Label(piezasframe, text="    ").grid(row=7,column=0)
                    espacio3=Label(piezasframe, text="    ").grid(row=9,column=0)

                    
                    

                    

                    
                    def tablac(): 
                        
                        global tabla

                        tabla=ttk.Treeview(piezasframe, columns=(1,2,3,4,5,6), show="headings")
                        
                        scroll=ttk.Scrollbar(piezasframe, orient=VERTICAL, command= tabla.yview)
                        scroll.grid(row=8, column=5, sticky=NS)
                        tabla.configure(yscrollcommand=scroll.set)



                        tabla.heading(1, text="id_pieza")
                        tabla.heading(2, text="Nombre_pieza")
                        tabla.heading(3, text="Estado")
                        tabla.heading(4, text="Peso (g)")
                        tabla.heading(5, text="Medidas")
                        tabla.heading(6, text="id_Componente")

                        tabla.column(1, width=150)
                        tabla.column(2, width=150)
                        tabla.column(3, width=150)
                        tabla.column(4, width=150)
                        tabla.column(5, width=150)
                        tabla.column(6, width=150)

                            
                            
                        for item in tabla.get_children():
                            tabla.delete(item)

                        registros=pieza.get_all_piezas()
                        
                        
                        

                        for registro in registros:
                            tabla.insert("", "end", values=registro)

                        tabla.grid(row=8,column=0,columnspan=3, sticky="nsew")
                        tabla.bind("<<TreeviewSelect>>", elementos)

                    
                    tablac()
                    elementos()



                elif frame==vehiculoframe:

                    def agregarbtn():
                        
                        vehiculo.insert(int(idVehiculoentry.get()),Tipo_Vehiculoentry.get(),int(idModeloentry.get()), int(Añoentry.get()))
                        
                        idVehiculoentry.delete(0,END)
                        Tipo_Vehiculoentry.delete(0,END)
                        idModeloentry.delete(0,END)
                        Añoentry.delete(0,END)
                        
                        tablac()
                        
                    def actualizar():
                        global tabla
                        Guardar.config(state=NORMAL)
                        
                        vehiculo.update(int(idVehiculoentry.get()),Tipo_Vehiculoentry.get(),int(idModeloentry.get()), int(Añoentry.get()))
                        Nuevo.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        tablac()
                        

                    def editarbtn():
                        global tabla
                        Guardar.config(state=NORMAL)
                        idVehiculoentry.config(state=NORMAL)
                        idModeloentry.config(state=NORMAL)
                        idVehiculoentry.delete(0,END)
                        Tipo_Vehiculoentry.delete(0,END)
                        idModeloentry.delete(0,END)
                        Añoentry.delete(0,END)
                        

                        idVehiculovalor=tabla.item(tabla.selection())['values'][0]
                        Tipo_Vehiculovalor=tabla.item(tabla.selection())['values'][1]
                        idModelovalor=tabla.item(tabla.selection())['values'][2]
                        Añoentryvalor=tabla.item(tabla.selection())['values'][3]
                        
                        idVehiculoentry.insert(0,idVehiculovalor)
                        Tipo_Vehiculoentry.insert(0,Tipo_Vehiculovalor)
                        idModeloentry.insert(0,idModelovalor)
                        Añoentry.insert(0,Añoentryvalor)
                        idVehiculoentry.config(state=DISABLED)
                        idModeloentry.config(state=DISABLED)
                        Nuevo.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        
                     
                    def borrarbtn():
                        global tabla
                        idVehiculo=tabla.item(tabla.selection())['values'][0]
                        if Vehiculoesparent(idVehiculo):
                            mensaje=messagebox.askyesno("Advertencia", "¿Estás seguro de que quieres eliminar este registro? Es un Parent Row, por lo que se eliminarán todos los Child Rows de otras tablas.")
                            if mensaje:
                                vehiculo.delete(idVehiculo)
                                
                            else:
                                pass
                        else:
                            vehiculo.delete(idVehiculo)

                        Nuevo.config(state=NORMAL)
                        tablac()
                           

                    def guardarbtn():
                        idVehiculoentry.config(state=NORMAL)
                        idModeloentry.config(state=NORMAL)
                        actualizar()
                        idVehiculoentry.delete(0,END)
                        Tipo_Vehiculoentry.delete(0,END)
                        idModeloentry.delete(0,END)
                        Añoentry.delete(0,END)
                        Guardar.config(state=DISABLED)
                        Nuevo.config(state=NORMAL)
                        Editar.config(state=DISABLED)
                        Eliminar.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        
                        
                    
                    registros=vehiculo.get_all_Vehiculos()



                    def nuevobtn():
                        idVehiculoentry.delete(0,END)
                        Tipo_Vehiculoentry.delete(0,END)
                        idModeloentry.delete(0,END)
                        Añoentry.delete(0,END)
                        
                        
                        Agregar.config(state=NORMAL)
                    
                    def elementos(event=NONE):
                        global tabla
                        if tabla.selection():
                            Editar.config(state=NORMAL)
                            Eliminar.config(state=NORMAL)

                    

                    def cancelarbtn():
                        global tabla
                        idVehiculoentry.config(state=NORMAL)
                        idModeloentry.config(state=NORMAL)
                        idVehiculoentry.delete(0,END)
                        Tipo_Vehiculoentry.delete(0,END)
                        idModeloentry.delete(0,END)
                        Añoentry.delete(0,END)
                        

                        tabla.selection_remove(tabla.selection())
                        Editar.config(state=DISABLED)
                        Eliminar.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        Nuevo.config(state=NORMAL)
                        
                            




                    idVehiculoentry=Entry(vehiculoframe, width=30)
                    Tipo_Vehiculoentry=Entry(vehiculoframe, width=30)
                    idModeloentry=Entry(vehiculoframe, width=30)
                    Añoentry=Entry(vehiculoframe, width=30)
                    
                    idVehiculoentry.grid(row=0,column=1)
                    Tipo_Vehiculoentry.grid(row=1,column=1)
                    idModeloentry.grid(row=2,column=1)
                    Añoentry.grid(row=3,column=1)
                    
                

                        
                    

                    idVehiculolabel=Label(vehiculoframe,text="idVehiculo (P)", fg="#000000", font=('crushed', 12, 'bold')).grid(row=0,column=0)
                    Tipo_Vehiculolabel=Label(vehiculoframe,text="Tipo_Vehiculo", fg="#000000", font=('crushed', 12, 'bold')).grid(row=1,column=0)
                    idModelolabel=Label(vehiculoframe,text="idModelo (F)", fg="#000000", font=('crushed', 12, 'bold')).grid(row=2,column=0)
                    Añolabel=Label(vehiculoframe,text="Año", fg="#000000", font=('crushed', 12, 'bold')).grid(row=3,column=0)
                    

                    ayudabtn=Button(vehiculoframe,text="?", padx=12,pady=1.5, command=ayudam, bg="#41c0b8", font=('crushed', 10))
                    ayudabtn.grid(row=1,column=2)   
                    Nuevo=Button(vehiculoframe, text="Nuevo", command=nuevobtn, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Nuevo.grid(row=4,column=0)
                    Agregar=Button(vehiculoframe, text="Agregar", command=agregarbtn, state=DISABLED,padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Agregar.grid(row=4, column=1)
                    Cancelar=Button(vehiculoframe, text="Cancelar", command=cancelarbtn, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Cancelar.grid(row=4,column=2)

                    Editar=Button(vehiculoframe, text="Editar", command=editarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Editar.grid(row=8,column=0)
                    Eliminar=Button(vehiculoframe, text="Eliminar", command=borrarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Eliminar.grid(row=8, column=1)
                    Guardar=Button(vehiculoframe, text="Guardar", command=guardarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Guardar.grid(row=8,column=2)
                    espacio2=Label(vehiculoframe, text="     ").grid(row=5,column=0)
                    espacio3=Label(vehiculoframe, text="     ").grid(row=7,column=0)

                    
                    

                    

                    
                    def tablac(): 
                        
                        global tabla

                        tabla=ttk.Treeview(vehiculoframe, columns=(1,2,3,4), show="headings")
                        
                        scroll=ttk.Scrollbar(vehiculoframe, orient=VERTICAL, command= tabla.yview)
                        scroll.grid(row=6, column=3, sticky=NSEW)
                        tabla.configure(yscrollcommand=scroll.set)

                        tabla.heading(1, text="idVehiculo")
                        tabla.heading(2, text="Tipo_Vehiculo")
                        tabla.heading(3, text="idModelo")
                        tabla.heading(4, text="Año")
                        
                            
                            
                        for item in tabla.get_children():
                            tabla.delete(item)

                        registros=vehiculo.get_all_Vehiculos()
                        
                        
                        

                        for registro in registros:
                            tabla.insert("", "end", values=registro)

                        tabla.grid(row=6,column=0,columnspan=3, sticky="nsew")
                        tabla.bind("<<TreeviewSelect>>", elementos)

                    
                    tablac()
                    elementos()


                    
                elif frame==marcaframe:

                    def agregarbtn():
                        
                        marca.insert(int(idMarcaentry.get()),Nombre_Marcaentry.get())
                        idMarcaentry.delete(0,END)
                        Nombre_Marcaentry.delete(0,END)
                        tablac()
                        
                    def actualizar():
                        global tabla
                        Guardar.config(state=NORMAL)
                        marca.update(Nombre_Marcaentry.get(),int(idMarcaentry.get()))
                        Nuevo.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        tablac()

                    def editarbtn():
                        global tabla
                        idMarcaentry.config(state=NORMAL)
                        Guardar.config(state=NORMAL)
                        idMarcaentry.delete(0,END)
                        Nombre_Marcaentry.delete(0,END)
                        idMarcavalor=tabla.item(tabla.selection())['values'][0]
                        Nombre_Marcavalor=tabla.item(tabla.selection())['values'][1]
                        
                        idMarcaentry.insert(0, idMarcavalor)
                        Nombre_Marcaentry.insert(0, Nombre_Marcavalor)
                        idMarcaentry.config(state=DISABLED)
                        Nuevo.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        
                     
                    def borrarbtn():
                        global tabla
                        id_marca=tabla.item(tabla.selection())['values'][0]
                        
                        if Marcaesparent(id_marca):
                            mensaje=messagebox.askyesno("Advertencia", "¿Estás seguro de que quieres eliminar este registro? Es un Parent Row, por lo que se eliminarán todos los Child Rows de otras tablas.")
                            if mensaje:
                                marca.delete(id_marca)
                            
                            else:
                                pass
                        else:
                            marca.delete(id_marca)
                        
                        Nuevo.config(state=NORMAL)
                        tablac()
                           

                    def guardarbtn():
                        idMarcaentry.config(state=NORMAL)
                        
                        
                        actualizar()
                        idMarcaentry.delete(0,END)
                        Nombre_Marcaentry.delete(0,END)
                        Editar.config(state=DISABLED)
                        Eliminar.config(state=DISABLED)
                        Guardar.config(state=DISABLED)
                        Nuevo.config(state=NORMAL)

                        
                        
                    
                    registros=marca.get_all_marca()



                    def nuevobtn():
                        idMarcaentry.config(state=NORMAL)
                        idMarcaentry.delete(0,END)
                        Nombre_Marcaentry.delete(0,END)
                        tabla.selection_remove(tabla.selection())
                        Agregar.config(state=NORMAL)
                    
                    def elementos(event=NONE):
                        global tabla
                        if tabla.selection():
                            Editar.config(state=NORMAL)
                            Eliminar.config(state=NORMAL)

                    

                    def cancelarbtn():
                        global tabla
                        idMarcaentry.config(state=NORMAL)
                        idMarcaentry.delete(0,END)
                        Nombre_Marcaentry.delete(0,END)
                        tabla.selection_remove(tabla.selection())
                        Editar.config(state=DISABLED)
                        Eliminar.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        Nuevo.config(state=NORMAL)
                        
                            





                    idMarcaentry=Entry(marcaframe, width=30)

                    Nombre_Marcaentry=Entry(marcaframe, width=30)

                    idMarcaentry.grid(row=0,column=1)
                    Nombre_Marcaentry.grid(row=1,column=1)

                    
                    def deleteentry():
                        idMarcaentry.insert(0,"")
                        
                    

                    idMarcalabel=Label(marcaframe,text="idMarca", fg="#000000", font=('crushed', 12, 'bold')).grid(row=0,column=0)
                    Nombre_Marcalabel=Label(marcaframe,text="Nombre_Marca", fg="#000000", font=('crushed', 12, 'bold')).grid(row=1,column=0)
                    
                    
                    ayudabtn=Button(marcaframe,text="?", padx=12,pady=1.5, command=ayudam, bg="#41c0b8", font=('crushed', 10))
                    ayudabtn.grid(row=1,column=2)   
                    Nuevo=Button(marcaframe, text="Nuevo", command=nuevobtn, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Nuevo.grid(row=4,column=0)
                    Agregar=Button(marcaframe, text="Agregar", command=agregarbtn, state=DISABLED,padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Agregar.grid(row=4, column=1)
                    Cancelar=Button(marcaframe, text="Cancelar", command=cancelarbtn, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Cancelar.grid(row=4,column=2)

                    Editar=Button(marcaframe, text="Editar", command=editarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Editar.grid(row=8,column=0)
                    Eliminar=Button(marcaframe, text="Eliminar", command=borrarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Eliminar.grid(row=8, column=1)
                    Guardar=Button(marcaframe, text="Guardar", command=guardarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Guardar.grid(row=8,column=2)
                    espacio2=Label(marcaframe, text="     ").grid(row=5,column=0)
                    espacio3=Label(marcaframe, text="     ").grid(row=7,column=0)

                    
                    

                    

                    
                    def tablac(): 
                        
                        global tabla

                        tabla=ttk.Treeview(marcaframe, columns=(1,2), show="headings")
                        
                        scroll=ttk.Scrollbar(marcaframe, orient=VERTICAL, command= tabla.yview)
                        scroll.grid(row=6, column=3, sticky=NSEW)
                        tabla.configure(yscrollcommand=scroll.set)

                        tabla.heading(1, text="idMarca")
                        tabla.heading(2, text="Nombre_Marca")
                            
                            
                        for item in tabla.get_children():
                            tabla.delete(item)

                        registros=marca.get_all_marca()
                        
                        
                        

                        for registro in registros:
                            tabla.insert("", "end", values=registro)

                        tabla.grid(row=6,column=0,columnspan=3, sticky="nsew")
                        tabla.bind("<<TreeviewSelect>>", elementos)

                    
                    tablac()
                    elementos()
                    
                    

                elif frame==componentesframe:
                    

                    def agregarbtn():
                        
                        componentes.insert(int(idComponenteentry.get()),Nombre_Componenteentry.get(),int(idVehiculoentry.get()))
                        idComponenteentry.delete(0,END)
                        Nombre_Componenteentry.delete(0,END)
                        idVehiculoentry.delete(0,END)
                        
                        tablac()
                        
                    def actualizar():
                        global tabla
                        Guardar.config(state=NORMAL)
                        
                        componentes.update(Nombre_Componenteentry.get(),int(idComponenteentry.get()))
                        Nuevo.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        tablac()
                        

                    def editarbtn():
                        global tabla
                        idComponenteentry.config(state=NORMAL)
                        idVehiculoentry.config(state=NORMAL)
                        Guardar.config(state=NORMAL)

                        idComponenteentry.delete(0,END)
                        Nombre_Componenteentry.delete(0,END)
                        idVehiculoentry.delete(0,END)
                        

                        idComponentevalor=tabla.item(tabla.selection())['values'][0]
                        Nombre_Componentevalor=tabla.item(tabla.selection())['values'][1]
                        idVehiculovalor=tabla.item(tabla.selection())['values'][2]
                        
                        idComponenteentry.insert(0, idComponentevalor)
                        Nombre_Componenteentry.insert(0, Nombre_Componentevalor)
                        idVehiculoentry.insert(0, idVehiculovalor)

                        idComponenteentry.config(state=DISABLED)
                        idVehiculoentry.config(state=DISABLED)
                        
                        Nuevo.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        
                     
                    def borrarbtn():
                        global tabla
                        idComponente=tabla.item(tabla.selection())['values'][0]
                        if Componentesesparent(idComponente):
                            mensaje=messagebox.askyesno("Advertencia", "¿Estás seguro de que quieres eliminar este registro? Es un Parent Row, por lo que se eliminarán todos los Child Rows de otras tablas.")
                            if mensaje:
                                componentes.delete(idComponente)
                                
                            else:
                                pass
                        else:
                            componentes.delete(idComponente)
                        
                        Nuevo.config(state=NORMAL)
                        tablac()
                           

                    def guardarbtn():
                        actualizar()
                        idComponenteentry.config(state=NORMAL)
                        idVehiculoentry.config(state=NORMAL)
                        idComponenteentry.delete(0,END)
                        Nombre_Componenteentry.delete(0,END)
                        idVehiculoentry.delete(0,END)
                        tabla.selection_remove(tabla.selection())
                        Editar.config(state=DISABLED)
                        Eliminar.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        
                        Guardar.config(state=DISABLED)
                        Nuevo.config(state=NORMAL)
                        
                        
                    
                    registros=componentes.get_all_componentes()



                    def nuevobtn():
                        idComponenteentry.delete(0,END)
                        Nombre_Componenteentry.delete(0,END)
                        idVehiculoentry.delete(0,END)
                        
                        
                        Agregar.config(state=NORMAL)
                    
                    def elementos(event=NONE):
                        global tabla
                        if tabla.selection():
                            Editar.config(state=NORMAL)
                            Eliminar.config(state=NORMAL)

                    

                    def cancelarbtn():
                        global tabla
                        idComponenteentry.config(state=NORMAL)
                        idVehiculoentry.config(state=NORMAL)
                        idComponenteentry.delete(0,END)
                        Nombre_Componenteentry.delete(0,END)
                        idVehiculoentry.delete(0,END)
                        

                        tabla.selection_remove(tabla.selection())
                        Editar.config(state=DISABLED)
                        Eliminar.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        Nuevo.config(state=NORMAL)
                        
                            





                    idComponenteentry=Entry(componentesframe, width=30)
                    Nombre_Componenteentry=Entry(componentesframe, width=30)
                    idVehiculoentry=Entry(componentesframe, width=30)
                    
                    
                    idComponenteentry.grid(row=0,column=1)
                    Nombre_Componenteentry.grid(row=1,column=1)
                    idVehiculoentry.grid(row=2,column=1)
                    

                        
                    

                    idComponenteslabel=Label(componentesframe,text="idComponentes (P)", fg="#000000", font=('crushed', 12, 'bold')).grid(row=0,column=0)
                    Nombre_Componenteslabel=Label(componentesframe,text="Nombre_Componentes", fg="#000000", font=('crushed', 12, 'bold')).grid(row=1,column=0)
                    idVehiculolabel=Label(componentesframe,text="idVehiculo (F)", fg="#000000", font=('crushed', 12, 'bold')).grid(row=2,column=0)
                    
                    
                    ayudabtn=Button(componentesframe,text="?", padx=12,pady=1.5, command=ayudam, bg="#41c0b8", font=('crushed', 10))
                    ayudabtn.grid(row=1,column=2)   
                    Nuevo=Button(componentesframe, text="Nuevo", command=nuevobtn, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Nuevo.grid(row=4,column=0)
                    Agregar=Button(componentesframe, text="Agregar", command=agregarbtn, state=DISABLED,padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Agregar.grid(row=4, column=1)
                    Cancelar=Button(componentesframe, text="Cancelar", command=cancelarbtn, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Cancelar.grid(row=4,column=2)

                    Editar=Button(componentesframe, text="Editar", command=editarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Editar.grid(row=8,column=0)
                    Eliminar=Button(componentesframe, text="Eliminar", command=borrarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Eliminar.grid(row=8, column=1)
                    Guardar=Button(componentesframe, text="Guardar", command=guardarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#c01616',fg="white", relief="raised",font=('crushed', 13))
                    Guardar.grid(row=8,column=2)
                    espacio2=Label(componentesframe, text="     ").grid(row=5,column=0)
                    espacio3=Label(componentesframe, text="     ").grid(row=7,column=0)

                    
                    

                    

                    
                    def tablac(): 
                        
                        global tabla

                        tabla=ttk.Treeview(componentesframe, columns=(1,2,3), show="headings")
                        
                        scroll=ttk.Scrollbar(componentesframe, orient=VERTICAL, command= tabla.yview)
                        scroll.grid(row=6, column=3, sticky=NSEW)
                        tabla.configure(yscrollcommand=scroll.set)

                        tabla.heading(1, text="idComponentes")
                        tabla.heading(2, text="Nombre_Componentes")
                        tabla.heading(3, text="idVehiculo")
                        
                            
                            
                        for item in tabla.get_children():
                            tabla.delete(item)

                        registros=componentes.get_all_componentes()
                        
                        
                        

                        for registro in registros:
                            tabla.insert("", "end", values=registro)

                        tabla.grid(row=6,column=0,columnspan=3, sticky="nsew")
                        tabla.bind("<<TreeviewSelect>>", elementos)

                    
                    tablac()
                    elementos()

              
                    
            
                
            



            #---------DEFINIENDO LOS FRAMES---------

            menuframe=Frame(root)
            consultasframe=Frame(root)
            ayudaframe=Frame(root)
            componentesframe=Frame(root)
            vehiculoframe=Frame(root)
            modeloframe=Frame(root)
            marcaframe=Frame(root)
            piezasframe=Frame(root)

            consultassframe=Frame(root)
            registrosframe=Frame(root)




            frames=[menuframe, consultasframe, ayudaframe, componentesframe, vehiculoframe, modeloframe, marcaframe, piezasframe, consultassframe, registrosframe]

            #-------------WIDGETS DE CONSULTASFRAME--------


            def registrosbtn():
                mostrarframe(registrosframe)

            def consultasbtn():
                mostrarframe(consultassframe)

            #labelconsultaframe=Label(consultasframe,text="Para extraer PDFs con información de las tablas, vaya a Registros. \nPara hacer consultas específicas de piezas, vaya a Consultas\n", fg='#000000',font=('crushed', 12, 'bold')).grid(row=0,column=0, columnspan=2)

            imagenconsultaframe=ImageTk.PhotoImage(Image.open("consultas.jpg"))
            labelconsultaframe=Label(consultasframe, image=imagenconsultaframe).grid(row=0,column=0, columnspan=5)
            registros=Button(consultasframe, text="Registros", command=registrosbtn,padx=17, pady=10, highlightthickness=0 , bg='#000000',fg="white", relief="raised",font=('crushed', 20))
            consultas=Button(consultasframe, text="Consultas", command=consultasbtn,padx=17, pady=10, highlightthickness=0 , bg='#000000',fg="white", relief="raised",font=('crushed', 20))

            esp1=Button(consultasframe, text="                   ", command=registrosbtn,state=DISABLED,padx=17, pady=10, highlightthickness=0 , bg='#131524',fg="white", relief="raised",font=('crushed', 20))
            esp2=Button(consultasframe, text="                   ", command=consultasbtn,state=DISABLED,padx=17, pady=10, highlightthickness=0 , bg='#131524',fg="white", relief="raised",font=('crushed', 20))
            esp3=Button(consultasframe, text="                   ", command=registrosbtn,state=DISABLED,padx=17, pady=10, highlightthickness=0 , bg='#131524',fg="white", relief="raised",font=('crushed', 20))
        
            esp1.grid(row=1, column=0)
            registros.grid(row=1,column=1)
            esp2.grid(row=1, column=2)
            consultas.grid(row=1, column=3)
            esp3.grid(row=1,column=4)


            #-----------------LO DE REGISTROS--------------------


            imagenpiezass=ImageTk.PhotoImage(Image.open("piezas.png"))
            imagenmodelos=ImageTk.PhotoImage(Image.open("modelo.png"))
            imagenmarcas=ImageTk.PhotoImage(Image.open("marca.png"))
            imagenvehiculos=ImageTk.PhotoImage(Image.open("carro.png"))
            imagencomponentess=ImageTk.PhotoImage(Image.open("componentes.png"))
            imagenrickrolls=ImageTk.PhotoImage(Image.open("rickroll.jpg"))

            label_imagenvehiculos=Label(registrosframe, image=imagenvehiculos).grid(row=5,column=1)
            label_imagenmodelos=Label(registrosframe, image=imagenmodelos).grid(row=5,column=2)
            label_imagenmarcas=Label(registrosframe, image=imagenmarcas).grid(row=5,column=3)
            label_imagenpiezass=Label(registrosframe, image=imagenpiezass).grid(row=5,column=4)
            label_imagencomponentess=Label(registrosframe,image=imagencomponentess).grid(row=5,column=5)
            

            labeleliges=Label(registrosframe,text="SELECCIONA UNA TABLA", font=('crushed', 20, 'bold')).grid(row=1,column=1, columnspan=5)
            labelespacio1s=Label(registrosframe,text="              ", font=('crushed', 20, 'bold')).grid(row=0,column=1, columnspan=5)
            labelespacio2s=Label(registrosframe,text="              ", font=('crushed', 20, 'bold')).grid(row=2,column=1, columnspan=5)
            labelespacio3s=Label(registrosframe,text="              ", font=('crushed', 20, 'bold')).grid(row=4,column=1, columnspan=5)

            vehiculoss=Button(registrosframe, text="VEHICULO",command=lambda:vehiculo.generate_vehiculo_pdf(), padx=17, pady=10, highlightthickness=0 , bg='#000000',fg="white", relief="raised",font=('crushed', 20))
            vehiculoss.grid(row=3,column=1)

            modeloss=Button(registrosframe, text="MODELO", command=lambda:modelo.generate_modelos_pdf(), padx=17, pady=10, highlightthickness=0 , bg='#000000',fg="white", relief="raised",font=('crushed', 20))
            modeloss.grid(row=3,column=2)

            marcass=Button(registrosframe, text="MARCA", command=lambda:marca.generate_marcas_pdf(), padx=17, pady=10, highlightthickness=0 , bg='#000000',fg="white", relief="raised",font=('crushed', 20))
            marcass.grid(row=3,column=3)

            piezasss=Button(registrosframe, text="PIEZAS", command=lambda:pieza.generate_pdf(), padx=17, pady=10, highlightthickness=0 , bg='#000000',fg="white", relief="raised",font=('crushed', 20))
            piezasss.grid(row=3,column=4)

            componentesss=Button(registrosframe, text="COMPONENTES", command=lambda:componentes.generate_componentes_pdf(), padx=14, pady=10, highlightthickness=0 , bg='#000000',fg="white", relief="raised",font=('crushed', 20))
            componentesss.grid(row=3,column=5)


            #-----------------LO DE CONSULTAS--------------------

            




            #---------DEFINIENDO LAS IMAGENES---------


           
            imagen2=ImageTk.PhotoImage(Image.open("menu.jpg"))

            imagenpiezas=ImageTk.PhotoImage(Image.open("piezas.png"))
            imagenmodelo=ImageTk.PhotoImage(Image.open("modelo.png"))
            imagenmarca=ImageTk.PhotoImage(Image.open("marca.png"))
            imagenvehiculo=ImageTk.PhotoImage(Image.open("carro.png"))
            imagencomponentes=ImageTk.PhotoImage(Image.open("componentes.png"))
            imagenrickroll=ImageTk.PhotoImage(Image.open("rickroll.jpg"))
            



            #---------DEFINIENDO Y MOSTRANDO LOS LABELS---------

            #Labels principales

            label_menuframe=Label(menuframe)
            label_menuframe.grid(row=0,column=0)
            
            
            label_ayudaframe=Label(ayudaframe)
            label_ayudaframe.grid(row=0,column=0)

            #Labels de las imagenes 

            label_imagenvehiculo=Label(menuframe, image=imagenvehiculo).grid(row=5,column=1)
            label_imagenmodelo=Label(menuframe, image=imagenmodelo).grid(row=5,column=2)
            label_imagenmarca=Label(menuframe, image=imagenmarca).grid(row=5,column=3)
            label_imagenpiezas=Label(menuframe, image=imagenpiezas).grid(row=5,column=4)
            label_imagencomponentes=Label(menuframe,image=imagencomponentes).grid(row=5,column=5)
            
            llabelrickroll=Label(ayudaframe, text="rickrolleado pa").grid(row=1,column=0)
            labelrickroll=Label(ayudaframe, image=imagenrickroll).grid(row=0, column=0)

            #Widgets del menuframe


            labelelige=Label(menuframe,text="SELECCIONA UNA TABLA", font=('crushed', 20, 'bold')).grid(row=1,column=1, columnspan=5)
            labelespacio1=Label(menuframe,text="              ", font=('crushed', 20, 'bold')).grid(row=0,column=1, columnspan=5)
            labelespacio2=Label(menuframe,text="              ", font=('crushed', 20, 'bold')).grid(row=2,column=1, columnspan=5)
            labelespacio3=Label(menuframe,text="              ", font=('crushed', 20, 'bold')).grid(row=4,column=1, columnspan=5)

            vehiculos=Button(menuframe, text="VEHICULO", command=tablavehiculo, padx=17, pady=10, highlightthickness=0 , bg='#000000',fg="white", relief="raised",font=('crushed', 20))
            vehiculos.grid(row=3,column=1)

            modelos=Button(menuframe, text="MODELO", padx=17,command=tablamodelo, pady=10, highlightthickness=0 , bg='#000000',fg="white", relief="raised",font=('crushed', 20))
            modelos.grid(row=3,column=2)

            marcas=Button(menuframe, text="MARCA", padx=17, pady=10,command=tablamarca, highlightthickness=0 , bg='#000000',fg="white", relief="raised",font=('crushed', 20))
            marcas.grid(row=3,column=3)

            piezass=Button(menuframe, text="PIEZAS", padx=17, pady=10,command=tablapiezas,highlightthickness=0 , bg='#000000',fg="white", relief="raised",font=('crushed', 20))
            piezass.grid(row=3,column=4)

            componentess=Button(menuframe, text="COMPONENTES", padx=14, pady=10,command=tablacomponentes, highlightthickness=0 , bg='#000000',fg="white", relief="raised",font=('crushed', 20))
            componentess.grid(row=3,column=5)




            #-----------------BARRA SUPERIOR-------------------


            BarraSuperior=Menu(root)

            BarraSuperior.add_command(label="Inicio", command=iniciobtn)
            BarraSuperior.add_command(label="Tablas", command=lambda:mostrarframe(menuframe))
            BarraSuperior.add_command(label="Consultas", command=lambda:mostrarframe(consultasframe))
            BarraSuperior.add_command(label="Extra", command=lambda:mostrarframe(ayudaframe))


            root.config(menu=BarraSuperior)


            root.mainloop()

            
    except mysql.connector.Error as e:
        print(f"Hubo un error en la conexión{e}")
    
    finally:  
        if db:
            db.close_connection()
            print("Finalizó la conexión.")
    

if __name__=="__main__":
    main()
