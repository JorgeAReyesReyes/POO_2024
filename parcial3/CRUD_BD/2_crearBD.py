import mysql.connector 

try:
    #conexion con la BD de MySQL
    conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
    
    #crear un onbjeto de tipo cursor para ejecutar SQL
    micursor=conexion.cursor()    

    sql="create database bd_python"

    micursor.execute(sql)

except Exception as e:
    print(f"Error:{e}")
    print(f"Tipo de error: {type(e).__name__}")
    print(f"ocurrio un error por favor vuelva intentar mas tarde")
else:
    print(f"se creo la BD exitosamente")
    micursor.execute("show databse")
    for x in micursor:
        print(x)