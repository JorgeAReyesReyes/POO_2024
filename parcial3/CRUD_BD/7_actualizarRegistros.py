from conexionBD import *

try:
   mycursor=conexion.cursor()
   sql="update clientes set direccion ='col. del UTD' where id=1"

   mycursor.execute(sql)
   #Es necesario ejecutar el commit para que finalice el sql con exito
   conexion.commit()

except:
    print(f"ocurrio un error por favor vuelva a intentar mas tarde...")
else:
    print("Registro eliminado con exito")