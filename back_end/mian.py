import mysql.connector
from back_end import Database
from piezas import Piezas
from marca import Marca
from modelo import Modelo
from vehiculo import Vehiculo
def main():
    
    db = Database("127.0.0.1","root","30412187","mydb")
    marca = Marca(db)
    pieza = Piezas(db)
    modelo = Modelo(db)
    vehiculo = Vehiculo(db)
    try:
        if db:
            vehiculo.insert()
            
    except mysql.connector.Error as e:
        print(f"hubo un error en la coneccion{e}")
    
    finally:  
        if db:
            db.close_connection()
            print("finalizo la conexion")
    

if __name__=="__main__":
    main()
    
    
    
    
    
    