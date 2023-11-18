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
import re
def main():
    
    db = Database("127.0.0.1","root","30412187","mydb")
    marca = Marca(db)
    pieza = Piezas(db)
    modelo = Modelo(db)
    vehiculo = Vehiculo(db)
    componentes = Componentes(db)
    
    try:
        if db:
            


            def mostrarframe(frame):
                
                for f in frames:
                    f.pack_forget()

                frame.pack()

            root= Tk()
            root.title("Menú")
            root.resizable(width=False, height=False)


            #MENU
            
            menuframe=Frame(root)
            vertablasframe=Frame(root)
            menu_imagen=ImageTk.PhotoImage(Image.open(r"C:\Users\PC\OneDrive\Escritorio\proyecto_BDD\back_end\menu.jpeg.jpg"))
            #definiendo los botones del menu
            def btn_vertablas():
                mostrarframe(vertablasframe)

            def btn_modificar():
                label_modificar=Label(root, text="asad")

            def btn_ayuda():
                label_ayuda=Label(root, text="adssad")

            def btn_salir():
                root.destroy()
            
            vertablas = Button(menuframe, text="VER TABLAS", command=btn_vertablas, padx=17, pady=6, highlightthickness=0 , bg='#895c47', font=('crushed', 20, 'bold'))
            vertablas.place(relx=0.1, rely=0.2, anchor=NW)
            
            
            

            modificar = Button(root, text="MODIFICAR", command=btn_modificar, padx=27, pady=9, highlightthickness=0 , bg='#895c47', font=('crushed', 20, 'bold'))
            modificar.place(relx=0.1, rely=0.41, anchor=NW)
            
            

            ayuda = Button(root, text="AYUDA", command=btn_ayuda, padx=48, pady=3, highlightthickness=0 , bg='#895c47', font=('crushed', 22, 'bold'))
            ayuda.place(relx=0.105, rely=0.63, anchor=NW)
            
            salir = Button(root, text="Salir", command=btn_salir, padx=55, pady=3, highlightthickness=0, bd=2, fg='red', bg='#a8996b', highlightbackground='red', font=('crushed', 20, 'bold'))
            salir.place(relx=0.92, rely=0.9, anchor=SE)
            
            
            label_menu=Label(menuframe, image=menu_imagen)
            label_menu.pack()
            vertablas.pack()
            vertablas.lift()




            #VERTABLAS

            
            #definiendo los botones de verframe
    
            imagentablas=ImageTk.PhotoImage(Image.open(r"C:\Users\PC\OneDrive\Escritorio\proyecto_BDD\back_end\empty.jpeg.jpg"))
            label_vertablas=Label(vertablasframe, image=imagentablas).pack()

            def btn_vermodelo():
                mostrarframe(vermodeloframe)
            def btn_vercomponentes():
                mostrarframe(vermodeloframe)
            def btn_vermarca():
                mostrarframe(vermarcaframe)
            def btn_verpiezas():
                mostrarframe(verpiezasframe)
            def btn_vervehiculo():
                mostrarframe(vervehiculoframe)

            vermodelo=Button(vertablasframe, text="VER MODELO", command=btn_vermodelo, padx=17, pady=6, highlightthickness=0 , bg='#895c47', font=('crushed', 20, 'bold'))
            vermodelo.place(relx=0.105, rely=0.205, anchor=NW)

            vercomponentes=Button(vertablasframe, text="VER COMPONENTES", command=btn_vercomponentes, padx=17, pady=6, highlightthickness=0 , bg='#895c47', font=('crushed', 20, 'bold'))
            vercomponentes.place(relx=0.105, rely=0.205, anchor=NW)

            vermarca=Button(vertablasframe, text="VER MARCA", command=btn_vermarca, padx=17, pady=6, highlightthickness=0 , bg='#895c47', font=('crushed', 20, 'bold'))
            vermarca.place(relx=0.35, rely=0.405, anchor=NW)

            verpiezas=Button(vertablasframe, text="VER PIEZAS", command=btn_verpiezas, padx=17, pady=6, highlightthickness=0 , bg='#895c47', font=('crushed', 20, 'bold'))
            verpiezas.place(relx=0.105, rely=0.205, anchor=CENTER)

            vervehiculo=Button(vertablasframe, text="VER VEHICULO", command=btn_vervehiculo, padx=17, pady=6, highlightthickness=0 , bg='#895c47', font=('crushed', 20, 'bold'))
            vervehiculo.place(relx=0.7, rely=0.405, anchor=NW)
            


            

        

            #definiendo los frames
            vermarcaframe=Frame(root)
            vercomponentesframe=Frame(root)
            vermodeloframe=Frame(root)
            verpiezasframe=Frame(root)
            vervehiculoframe=Frame(root)
            ayudaframe=Frame(root)
            modframe=Frame(root)
            modcomponentesframe=Frame(root)
            modmodeloframe=Frame(root)
            modpiezasframe=Frame(root)
            modvehiculoframe=Frame(root)
            modmarcaframe=Frame(root)
            frames=[menuframe,vertablasframe, vercomponentesframe, vermodeloframe, verpiezasframe, vervehiculoframe, vermarcaframe, modframe, modcomponentesframe, modmodeloframe, modpiezasframe, modvehiculoframe, modmarcaframe, ayudaframe]

            

            

            mostrarframe(menuframe)

            
            





            root.mainloop()
            
    except mysql.connector.Error as e:
        print(f"hubo un error en la coneccion{e}")
    
    finally:  
        if db:
            db.close_connection()
            print("finalizo la conexion")
    

if __name__=="__main__":
    main()

