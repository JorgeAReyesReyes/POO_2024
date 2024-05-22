 #Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y 
 # luego las multiplicaciones del 1 al 10


for i in range(1, 11):
    print(f"Tabla del {i}:")
    for n2 in range(1, 11):
        print(f"{i} x {n2} = {i*n2}")
    print()
