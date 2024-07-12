from conexionBD import *

try:
   mycursor=conexion.cursor()
   sql="insert into clientes(id, nombre ,direccion,tel) values (null,'juan polaina', 'col del valle', '6181234567')"

   mycursor.execute(sql)
   #Es necesario ejecutar el commit para que finalice el sql con exito
   conexion.commit()
except:
    print(f"ocurrio un error por favor vuelva a intentar mas tarde...")
else:
    print("Registro insertado con exito")