#Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?


n2=input("solicitar porcentaje: ")
n1=input("solicitar numero: ")

porcentaje=(float(n2)*float(n1))/100

text=('el '+n2+'% de '+n1+' es:')
print(text)
print(float(porcentaje))