#Escribe un programa que reciba una cantidad de minutos y muestre por pantalla a 
#cuantas horas y minutos corresponde.
print ("Programa 07")
print("")
num = int(input("Introduce la cantidad en minutos"))
horas = int(num/60)
min = num % 60
print (horas,":",min)

#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente 
#desea saber cuanto deberá pagar finalmente por su compra.
print ("Programa 08")
print("")
num = float(input("introduce el valor de tu compra: "))
pago = num - (num *0.15)
print ("vas a pagar: ", pago, "€")

#Escribe un programa que calcule la calificación de estudiante en un módulo. La 
#calificación se obtiene de la calificación parcial en cada RA (RA1 20%, RA2, 60% y RA3 20%).
# Pedir notas al usuario
ra1 = float(input("Introduce la calificación de RA1: "))
ra2 = float(input("Introduce la calificación de RA2: "))
ra3 = float(input("Introduce la calificación de RA3: "))

calific = (ra1 * 0.2) + (ra2 * 0.6) + (ra3 * 0.2)

print("La calificación final del módulo es:", calific)
