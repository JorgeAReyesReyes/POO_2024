# Crear un programa que solicite la calificacion de 15 alumnos e 
# imprimir en pantalla cuantos aproboron y cuantos no aprobaron

nota = 0
aprobados = 0
reprobados = 0

input_scanner = input

for i in range(0,15):
    print(f"Nota del alumno No. {i+1} : ", end="")
    nota = float(input_scanner())
    
    if 1 <= nota < 80.0:
        reprobados += 1
    elif 3 <= nota >=80:
        aprobados += 1

print("\nAlumnos reprobados:", reprobados)
print("Alumnos aprobados:", aprobados)

