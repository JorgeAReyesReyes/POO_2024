import mysql.connector 

try:
    #conexion con la BD de MySQL
    conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_python"
)
except Exception as e:
    print(f"Tipo de error: {type(e).__name__}")
    print(f"ocurrio un error por favor vuelva intentar mas tarde")
#verificar si la conexion es correcta
if conexion.is_connected():
    print(f"se creo la conexion exitosamente...")
else:
    print(f"no fue posible conectar con la BD...verifique")