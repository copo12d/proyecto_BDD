import mysql.connector
from back_end import Database
from piezas import Piezas
from marca import Marca
from modelo import Modelo
from vehiculo import Vehiculo
from componentes import Componentes
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import re



def main():
    
    db = Database("127.0.0.1","root","30412187","actucascada")
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
            image4=ImageTk.PhotoImage(Image.open("menu.jpg"))
            label_inicio=Label(root, image=image4)
            label_inicio.pack()
            ancho=image4.width()
            alto=image4.height()
            root.geometry(f"{ancho}x{alto}+100+100")
            print(alto,ancho)
            rickroll=ImageTk.PhotoImage(Image.open("rickroll.jpg"))

            #---------DEFINIENDO LA FUNCION PARA MOSTRAR LOS FRAMES (Y ELIMINAR LA IMAGEN DE INICIO)---------

            def mostrarframe(frame):
                
                for f in frames:
                    f.pack_forget()
                frame.pack(expand=False)
                label_inicio.pack_forget()
                if frame==vehiculoframe or frame==componentesframe or frame==piezasframe or frame==marcaframe or frame==modeloframe:
                    widgetstablas(frame)
                    
                


            def iniciobtn():
                
                for f in frames:
                    f.pack_forget()

                label_inicio.pack()

        





            #---------FUNCIONES DE LOS BOTONES DEl MENU---------

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




            


            


             #---------WIDGETS DE LOS FRAMES DE LAS TABLAS---------

            entrys=[]

            def widgetstablas(frame):
                global tam
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
                        
                        Nuevo.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        
                     
                    def borrarbtn():
                        global tabla
                        id_modelo=tabla.item(tabla.selection())['values'][0]
                        modelo.delete(id_modelo)
                        Nuevo.config(state=NORMAL)
                        tablac()
                           

                    def guardarbtn():
                        actualizar()
                        Guardar.config(state=DISABLED)
                        Nuevo.config(state=NORMAL)
                        
                        
                    
                    registros=modelo.get_all_modelos()



                    def nuevobtn():
                        idModeloentry.delete(0,END)
                        Nombre_Modeloentry.delete(0,END)
                        idMarcaentry.delete(0,END)
                        
                        
                        Agregar.config(state=NORMAL)
                    
                    def elementos(event=NONE):
                        global tabla
                        if tabla.selection():
                            Editar.config(state=NORMAL)
                            Eliminar.config(state=NORMAL)

                    

                    def cancelarbtn():
                        global tabla
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
                    

                        
                    

                    idModelolabel=Label(modeloframe,text="idModelo (P)", fg="#134265", font=('crushed', 12, 'bold')).grid(row=0,column=0)
                    Nombre_Modelolabel=Label(modeloframe,text="Nombre_Modelo", fg="#134265", font=('crushed', 12, 'bold')).grid(row=1,column=0)
                    idMarcalabel=Label(modeloframe,text="idMarca (F)", fg="#134265", font=('crushed', 12, 'bold')).grid(row=2,column=0)
                    
                    

                    Nuevo=Button(modeloframe, text="Nuevo", command=nuevobtn, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Nuevo.grid(row=4,column=0)
                    Agregar=Button(modeloframe, text="Agregar", command=agregarbtn, state=DISABLED,padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Agregar.grid(row=4, column=1)
                    Cancelar=Button(modeloframe, text="Cancelar", command=cancelarbtn, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Cancelar.grid(row=4,column=2)

                    Editar=Button(modeloframe, text="Editar", command=actualizar, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Editar.grid(row=8,column=0)
                    Eliminar=Button(modeloframe, text="Eliminar", command=borrarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Eliminar.grid(row=8, column=1)
                    Guardar=Button(modeloframe, text="Guardar", command=guardarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
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
                        
                        pieza.insert(int(id_piezasentry.get()),nombre_piezaentry.get(),descripcionentry.get(), int(id_Componenteentry.get()))
                        
                        id_piezasentry.delete(0,END)
                        nombre_piezaentry.delete(0,END)
                        descripcionentry.delete(0,END)
                        id_Componenteentry.delete(0,END)
                        
                        tablac()
                        

                    def editarbtn():
                        global tabla
                        Guardar.config(state=NORMAL)
                        id_piezasentry.delete(0,END)
                        nombre_piezaentry.delete(0,END)
                        descripcionentry.delete(0,END)
                        id_Componenteentry.delete(0,END)
                        

                        idpiezasvalor=tabla.item(tabla.selection())['values'][0]
                        nombrepiezavalor=tabla.item(tabla.selection())['values'][1]
                        descripcionvalor=tabla.item(tabla.selection())['values'][2]
                        idcomponentevalor=tabla.item(tabla.selection())['values'][3]
                        

                        id_piezasentry.insert(0,idpiezasvalor)
                        nombre_piezaentry.insert(0,nombrepiezavalor)
                        descripcionentry.insert(0,descripcionvalor)
                        id_Componenteentry.insert(0,idcomponentevalor)
                        
                        Nuevo.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        
                     
                    def borrarbtn():
                        global tabla
                        idpiezas=tabla.item(tabla.selection())['values'][0]
                        pieza.delete(idpiezas)
                        Nuevo.config(state=NORMAL)
                        tablac()
                           

                    def guardarbtn():
                        borrarbtn()  
                        agregarbtn()
                        Guardar.config(state=DISABLED)
                        Nuevo.config(state=NORMAL)
                        
                        
                    
                    registros=pieza.get_all_piezas()



                    def nuevobtn():
                        id_piezasentry.delete(0,END)
                        nombre_piezaentry.delete(0,END)
                        descripcionentry.delete(0,END)
                        id_Componenteentry.delete(0,END)
                        
                        Agregar.config(state=NORMAL)
                    
                    def elementos(event=NONE):
                        global tabla
                        if tabla.selection():
                            Editar.config(state=NORMAL)
                            Eliminar.config(state=NORMAL)

                    

                    def cancelarbtn():
                        global tabla
                        id_piezasentry.delete(0,END)
                        nombre_piezaentry.delete(0,END)
                        descripcionentry.delete(0,END)
                        id_Componenteentry.delete(0,END)
                        

                        tabla.selection_remove(tabla.selection())
                        Editar.config(state=DISABLED)
                        Eliminar.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        Nuevo.config(state=NORMAL)
                        
                            


                    id_piezasentry=Entry(piezasframe, width=30)
                    nombre_piezaentry=Entry(piezasframe, width=30)
                    descripcionentry=Entry(piezasframe, width=30)
                    id_Componenteentry=Entry(piezasframe, width=30)
                    
                    id_piezasentry.grid(row=0,column=1)
                    nombre_piezaentry.grid(row=1,column=1)
                    descripcionentry.grid(row=2,column=1)
                    id_Componenteentry.grid(row=3,column=1)
                    
                

                    id_piezaslabel=Label(piezasframe,text="id_pieza (P)", fg="#134265", font=('crushed', 12, 'bold')).grid(row=0,column=0)
                    nombre_piezalabel=Label(piezasframe,text="nombre_pieza", fg="#134265", font=('crushed', 12, 'bold')).grid(row=1,column=0)
                    descripcionlabel=Label(piezasframe,text="descripción", fg="#134265", font=('crushed', 12, 'bold')).grid(row=2,column=0)
                    id_Componentelabel=Label(piezasframe,text="idComponente (F)", fg="#134265", font=('crushed', 12, 'bold')).grid(row=3,column=0)
                    
                    

                    Nuevo=Button(piezasframe, text="Nuevo", command=nuevobtn, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Nuevo.grid(row=4,column=0)
                    Agregar=Button(piezasframe, text="Agregar", command=agregarbtn, state=DISABLED,padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Agregar.grid(row=4, column=1)
                    Cancelar=Button(piezasframe, text="Cancelar", command=cancelarbtn, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Cancelar.grid(row=4,column=2)

                    Editar=Button(piezasframe, text="Editar", command=editarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Editar.grid(row=8,column=0)
                    Eliminar=Button(piezasframe, text="Eliminar", command=borrarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Eliminar.grid(row=8, column=1)
                    Guardar=Button(piezasframe, text="Guardar", command=guardarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Guardar.grid(row=8,column=2)
                    espacio2=Label(piezasframe, text="     ").grid(row=5,column=0)
                    espacio3=Label(piezasframe, text="     ").grid(row=7,column=0)

                    
                    

                    

                    
                    def tablac(): 
                        
                        global tabla

                        tabla=ttk.Treeview(piezasframe, columns=(1,2,3,4), show="headings")
                        
                        scroll=ttk.Scrollbar(piezasframe, orient=VERTICAL, command= tabla.yview)
                        scroll.grid(row=6, column=3, sticky=NSEW)
                        tabla.configure(yscrollcommand=scroll.set)

                        tabla.heading(1, text="id_pieza")
                        tabla.heading(2, text="Nombre_pieza")
                        tabla.heading(3, text="descripcion")
                        tabla.heading(4, text="id_Componente")
                        
                            
                            
                        for item in tabla.get_children():
                            tabla.delete(item)

                        registros=pieza.get_all_piezas()
                        
                        
                        

                        for registro in registros:
                            tabla.insert("", "end", values=registro)

                        tabla.grid(row=6,column=0,columnspan=3, sticky="nsew")
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
                        idVehiculoentry.delete(0,END)
                        Tipo_Vehiculoentry.delete(0,END)
                        idModeloentry.delete(0,END)
                        Añoentry.delete(0,END)
                        

                        idVehiculovalor=tabla.item(tabla.selection())['values'][0]
                        Tipo_Vehiculovalor=tabla.item(tabla.selection())['values'][1]
                        idModelovalor=tabla.item(tabla.selection())['values'][2]
                        Añoentryvalor=tabla.item(tabla.selection())['values'][2]
                        
                        idVehiculoentry.insert(0,idVehiculovalor)
                        Tipo_Vehiculoentry.insert(0,Tipo_Vehiculovalor)
                        idModeloentry.insert(0,idModelovalor)
                        Añoentry.insert(0,Añoentryvalor)
                        
                        Nuevo.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        
                     
                    def borrarbtn():
                        global tabla
                        idVehiculo=tabla.item(tabla.selection())['values'][0]
                        vehiculo.delete(idVehiculo)
                        Nuevo.config(state=NORMAL)
                        tablac()
                           

                    def guardarbtn():
                        
                        actualizar()
                        
                        Guardar.config(state=DISABLED)
                        Nuevo.config(state=NORMAL)
                        
                        
                    
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
                    
                

                        
                    

                    idVehiculolabel=Label(vehiculoframe,text="idVehiculo (P)", fg="#134265", font=('crushed', 12, 'bold')).grid(row=0,column=0)
                    Tipo_Vehiculolabel=Label(vehiculoframe,text="Tipo_Vehiculo", fg="#134265", font=('crushed', 12, 'bold')).grid(row=1,column=0)
                    idModelolabel=Label(vehiculoframe,text="idModelo (F)", fg="#134265", font=('crushed', 12, 'bold')).grid(row=2,column=0)
                    Añolabel=Label(vehiculoframe,text="Año", fg="#134265", font=('crushed', 12, 'bold')).grid(row=3,column=0)
                    

                    Nuevo=Button(vehiculoframe, text="Nuevo", command=nuevobtn, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Nuevo.grid(row=4,column=0)
                    Agregar=Button(vehiculoframe, text="Agregar", command=agregarbtn, state=DISABLED,padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Agregar.grid(row=4, column=1)
                    Cancelar=Button(vehiculoframe, text="Cancelar", command=cancelarbtn, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Cancelar.grid(row=4,column=2)

                    Editar=Button(vehiculoframe, text="Editar", command=actualizar, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Editar.grid(row=8,column=0)
                    Eliminar=Button(vehiculoframe, text="Eliminar", command=borrarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Eliminar.grid(row=8, column=1)
                    Guardar=Button(vehiculoframe, text="Guardar", command=guardarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
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
                        Guardar.config(state=NORMAL)
                        
                        idMarcavalor=tabla.item(tabla.selection())['values'][0]
                        Nombre_Marcavalor=tabla.item(tabla.selection())['values'][1]
                        idMarcaentry.insert(0, idMarcavalor)
                        Nombre_Marcaentry.insert(0, Nombre_Marcavalor)
                        Nuevo.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        
                     
                    def borrarbtn():
                        global tabla
                        id_marca=tabla.item(tabla.selection())['values'][0]
                        marca.delete(id_marca)
                        Nuevo.config(state=NORMAL)
                        tablac()
                           

                    def guardarbtn():
                        
                        actualizar()
                        
                        Guardar.config(state=DISABLED)
                        Nuevo.config(state=NORMAL)
                        
                        
                    
                    registros=marca.get_all_marca()



                    def nuevobtn():
                        idMarcaentry.delete(0,END)
                        Nombre_Marcaentry.delete(0,END)
                        
                        Agregar.config(state=NORMAL)
                    
                    def elementos(event=NONE):
                        global tabla
                        if tabla.selection():
                            Editar.config(state=NORMAL)
                            Eliminar.config(state=NORMAL)

                    

                    def cancelarbtn():
                        global tabla
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
                        
                    

                    idMarcalabel=Label(marcaframe,text="idMarca", fg="#134265", font=('crushed', 12, 'bold')).grid(row=0,column=0)
                    Nombre_Marcalabel=Label(marcaframe,text="Nombre_Marca", fg="#134265", font=('crushed', 12, 'bold')).grid(row=1,column=0)
                    
                    

                    Nuevo=Button(marcaframe, text="Nuevo", command=nuevobtn, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Nuevo.grid(row=4,column=0)
                    Agregar=Button(marcaframe, text="Agregar", command=agregarbtn, state=DISABLED,padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Agregar.grid(row=4, column=1)
                    Cancelar=Button(marcaframe, text="Cancelar", command=cancelarbtn, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Cancelar.grid(row=4,column=2)

                    Editar=Button(marcaframe, text="Editar", command=actualizar, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Editar.grid(row=8,column=0)
                    Eliminar=Button(marcaframe, text="Eliminar", command=borrarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Eliminar.grid(row=8, column=1)
                    Guardar=Button(marcaframe, text="Guardar", command=guardarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
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
                        
                        Nuevo.config(state=DISABLED)
                        Agregar.config(state=DISABLED)
                        
                     
                    def borrarbtn():
                        global tabla
                        idComponente=tabla.item(tabla.selection())['values'][0]
                        componentes.delete(idComponente)
                        Nuevo.config(state=NORMAL)
                        tablac()
                           

                    def guardarbtn():
                        
                        actualizar()
                        
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
                    

                        
                    

                    idComponenteslabel=Label(componentesframe,text="idComponentes (P)", fg="#134265", font=('crushed', 12, 'bold')).grid(row=0,column=0)
                    Nombre_Componenteslabel=Label(componentesframe,text="Nombre_Componentes", fg="#134265", font=('crushed', 12, 'bold')).grid(row=1,column=0)
                    idVehiculolabel=Label(componentesframe,text="idVehiculo (F)", fg="#134265", font=('crushed', 12, 'bold')).grid(row=2,column=0)
                    
                    

                    Nuevo=Button(componentesframe, text="Nuevo", command=nuevobtn, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Nuevo.grid(row=4,column=0)
                    Agregar=Button(componentesframe, text="Agregar", command=agregarbtn, state=DISABLED,padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Agregar.grid(row=4, column=1)
                    Cancelar=Button(componentesframe, text="Cancelar", command=cancelarbtn, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Cancelar.grid(row=4,column=2)

                    Editar=Button(componentesframe, text="Editar", command=actualizar, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Editar.grid(row=8,column=0)
                    Eliminar=Button(componentesframe, text="Eliminar", command=borrarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
                    Eliminar.grid(row=8, column=1)
                    Guardar=Button(componentesframe, text="Guardar", command=guardarbtn, state=DISABLED, padx=17, pady=10, highlightthickness=0 , bg='#ff3f4a',fg="white", relief="raised",font=('crushed', 13))
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



            frames=[menuframe, consultasframe, ayudaframe, componentesframe, vehiculoframe, modeloframe, marcaframe, piezasframe]




            #---------DEFINIENDO LAS IMAGENES---------


           
            imagen2=ImageTk.PhotoImage(Image.open("menu.jpg"))

            imagenpiezas=ImageTk.PhotoImage(Image.open("piezas.png"))
            imagenmodelo=ImageTk.PhotoImage(Image.open("modelo.png"))
            imagenmarca=ImageTk.PhotoImage(Image.open("marca.png"))
            imagenvehiculo=ImageTk.PhotoImage(Image.open("carro.png"))
            imagencomponentes=ImageTk.PhotoImage(Image.open("componentes.png"))
            imagenrickroll=ImageTk.PhotoImage(Image.open("rickroll.jpg"))




            #---------DEFINIENDO Y MOSTRANDO LOS LABELS---------

            label_menuframe=Label(menuframe)
            label_menuframe.grid(row=0,column=0)
            label_consultasframe=Label(consultasframe)
            label_consultasframe.grid(row=0,column=0)
            label_ayudaframe=Label(ayudaframe)
            label_ayudaframe.grid(row=0,column=0)

            label_imagenvehiculo=Label(menuframe, image=imagenvehiculo).grid(row=5,column=1)
            label_imagenmodelo=Label(menuframe, image=imagenmodelo).grid(row=5,column=2)
            label_imagenmarca=Label(menuframe, image=imagenmarca).grid(row=5,column=3)
            label_imagenpiezas=Label(menuframe, image=imagenpiezas).grid(row=5,column=4)
            label_imagencomponentes=Label(menuframe,image=imagencomponentes).grid(row=5,column=5)
            llabelrickroll=Label(ayudaframe, text="rickrolleado pa").grid(row=0,column=0)
            labelrickroll=Label(ayudaframe, image=imagenrickroll).grid(row=1, column=0)





            labelelige=Label(menuframe,text="ELIGE LA TABLA", bg="#92b0c6", font=('crushed', 20, 'bold')).grid(row=1,column=1, columnspan=5)
            labelespacio1=Label(menuframe,text="              ", font=('crushed', 20, 'bold')).grid(row=0,column=1, columnspan=5)
            labelespacio2=Label(menuframe,text="              ", font=('crushed', 20, 'bold')).grid(row=2,column=1, columnspan=5)
            labelespacio3=Label(menuframe,text="              ", font=('crushed', 20, 'bold')).grid(row=4,column=1, columnspan=5)

            vehiculos=Button(menuframe, text="VEHICULO", command=tablavehiculo, padx=17, pady=10, highlightthickness=0 , bg='#2a4e68',fg="white", relief="raised",font=('crushed', 20))
            vehiculos.grid(row=3,column=1)

            modelos=Button(menuframe, text="MODELO", command=tablamodelo, padx=17, pady=10, highlightthickness=0 , bg='#2a4e68',fg="white", relief="raised",font=('crushed', 20))
            modelos.grid(row=3,column=2)

            marcas=Button(menuframe, text="MARCA", command=tablamarca, padx=17, pady=10, highlightthickness=0 , bg='#2a4e68',fg="white", relief="raised",font=('crushed', 20))
            marcas.grid(row=3,column=3)

            piezass=Button(menuframe, text="PIEZAS", command=tablapiezas, padx=17, pady=10, highlightthickness=0 , bg='#2a4e68',fg="white", relief="raised",font=('crushed', 20))
            piezass.grid(row=3,column=4)

            componentess=Button(menuframe, text="COMPONENTES", command=tablacomponentes, padx=14, pady=10, highlightthickness=0 , bg='#2a4e68',fg="white", relief="raised",font=('crushed', 20))
            componentess.grid(row=3,column=5)







            BarraSuperior=Menu(root)
            BarraInferior=Menu(root)

            BarraSuperior.add_command(label="Inicio", command=iniciobtn)
            BarraSuperior.add_command(label="Tablas", command=lambda:mostrarframe(menuframe))
            BarraSuperior.add_command(label="Consultas", command=lambda:mostrarframe(consultasframe))
            BarraSuperior.add_command(label="Ayuda", command=lambda:mostrarframe(ayudaframe))





            root.config(menu=BarraSuperior)


            root.mainloop()

            def submit():
                #clear the text boxes
                try: 
                    '''componentes.insert(int(id_.get()), Nombre_Componente.get(), int(Vehiculo_idVehiculo.get()), int(Vehiculo_Modelo_idModelo.get()))
                    idComponente.delete(0,END)
                    Nombre_Componente.delete(0,END)
                    Vehiculo_idVehiculo.delete(0,END)
                    Vehiculo_Modelo_idModelo.delete(0,END)'''

                except:
                    messagebox.showerror("Error", "Intentalo de nuevo.")
                    '''idComponente.delete(0,END)
                    Nombre_Componente.delete(0,END)
                    Vehiculo_idVehiculo.delete(0,END)
                    Vehiculo_Modelo_idModelo.delete(0,END)'''



            


            
            
    except mysql.connector.Error as e:
        print(f"hubo un error en la coneccion{e}")
    
    finally:  
        if db:
            db.close_connection()
            print("finalizo la conexion")
    

if __name__=="__main__":
    main()
    
            
    


    
    
    