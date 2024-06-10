
opc=0
n=0

while opc !="no":
 name=input("nombre del paciente: ")

 t_sangre=input("tipo de sangre del paciente(o,A,B, AB): ")
 RH=input("RH(positivo/negativo): ")
 print("tipo de sangre: "+str(t_sangre)+str(RH))

 "valores normales sistolica=120 diastolica =80"

 presionSis_1=input("primera presion sitolica: ")
 presiondis_1=input("primera presion diastolica: ")
 print(presionSis_1)
 print(presiondis_1)

 presionSis_2=input("segunda presion sitolica: ")
 presiondis_2=input("segunda presion diastolica: ")
 print(presionSis_1)
 print(presiondis_1)

 presionSis_3=input("tercera  presion sitolica: ")
 presiondis_3=input("tercera presion diastolica: ")
 print(presionSis_1)
 print(presiondis_1)

 presionsis_f=input("presion sistolica al final del dia igual:")
 presiondis_f=input("presion distolica al final del dia igual:")
 print(presionsis_f)
 print(presiondis_f)

 promedio_presionSis=(int(presionSis_1)+int(presionSis_2)+int(presionSis_3))/3
 promedio_presiondis=(int(presiondis_1)+int(presiondis_2)+int(presiondis_3))/3
 print("promedio de presion sistolica: "+str(promedio_presionSis))
 print("promedio de presion diastolica: "+str(promedio_presiondis))

 presion_sis_f=(int(promedio_presionSis)+int(presionsis_f))/2
 presion_dis_f=(int(promedio_presiondis)+int(presiondis_f))/2

 print(presion_sis_f)
 print(presion_dis_f)
 if presion_sis_f<=120 and presion_dis_f<=80:
    print("valores normales sistolica=120 diastolica =80")
    print("presion normal")
 opc=input("¿desea introducir otro paciente?(si/no)")
 print=str(opc)
 if opc== 'no':
    break
 pacientes_capturados=n+1
 
print("pacientes capturados: " + str(pacientes_capturados))
 


