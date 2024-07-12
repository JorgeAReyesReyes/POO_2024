from conexionBD import *

try:
   mycursor=conexion.cursor()
   sql="select * from clientes"

   mycursor.execute(sql)
   
   resultado=mycursor.fetchall()
   
   for fila in resultado:
       print(f"id:{fila[0]} |nombre:{fila[1]} |Direccion{fila[2]} |telefono:{fila[ 3]}")

except:
    print(f"ocurrio un error por favor vuelva a intentar mas tarde...")
else:
    print("Registros consultados con exito")