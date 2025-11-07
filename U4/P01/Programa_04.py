#Escribe un programa en Python que realice las siguientes operaciones con cadenas:
#Convierte un número entero, un número decimal y un booleano en cadenas 
#(str()).
#Convierte una cadena en entero y en decimal (int(), float()).
#Crea una cadena cruda (r"...") que contenga caracteres especiales y muéstrala.

entero = 25
decimal = 25.50
booleano = True

cadena1 = str(entero) +" " + str(decimal)+ " " + str(booleano)
print ("imprimiendo el resultado: {} ".format(cadena1))