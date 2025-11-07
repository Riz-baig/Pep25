#Declara una cadena "  Hola Mundo  ".
#Aplica y muestra los resultados de: upper(), lower(), capitalize(), 
#title().
#Elimina espacios con strip().
#Sustituye "Mundo" por "Python" con replace().
#Divide la cadena en palabras con split().
#Une una lista de palabras con join().

cadena1 = " Hola Mundo "
print("Mayuscuals: ", cadena1.upper())
print("Minusculas: ", cadena1.lower())
print("Primera letra mayuscula: ", cadena1.capitalize())
print("primera letra de cada palabra mayusculas: ", cadena1.title())
print("Elimina los espacios.", cadena1.strip())
print("")
print("sustitute la palabra mundo por python: ", cadena1.replace("Mundo", "Python"))
lista = cadena1.split(" ")
print("Divide la cadena: ", lista)
cadena2 = "".join(lista)
print("une la cadena lista: ", cadena2)