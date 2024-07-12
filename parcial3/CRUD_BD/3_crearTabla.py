
from conexionBD import *

try:
   mycursor=conexion.cursor()
   sql="create table clientes(id int primary key auto_increment, nombre varchar (60),direccion varchar(120),tel varchar(10))"

   mycursor.execute(sql)
except:
    print(f"ocurrio un error por favor vuelva a intentar mas tarde...")
else:
    print("se creo la tabla con exito")