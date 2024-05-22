#Hacer un programa que solicite numeros indefinidamente hasta 
# que se introduzca el 111 y salir del programa


i=1

while i !=111:
 i=input("escribir numero: ")
 i=int(i)
 print(i)
 if i==111:
     break
print("accion finalizada")


