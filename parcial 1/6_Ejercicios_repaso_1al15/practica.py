#crear un programa que permita calcular el precio a pagar por un articulo
#en el precio a pagar se incluye el iva.el programa debera de funcionar n veces como el usuario desee
i=0
str(i)

while i !="si":
 producto=input("producto: ")
 precio_p=(input("precio del producto:"))
 int(precio_p)
 iva=int(precio_p)*0.16
 precio_neto=float(iva)+float(precio_p)

 print('producto: '+producto)
 print('total a pagar: '+str(precio_neto))
 opc=input("ingreas otro producto(si/no): ")
 if opc=="no":
     break
print("gracias poe su compra vuelva pronto ")
 

