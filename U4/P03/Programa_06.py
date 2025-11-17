#Escribe un programa en Python que realice las siguientes operaciones con listas:
#Crea un cadena de caracteres con varias palabras y a partir de ella crear una lista 
#que contenga como elementos las palabras de la cadena.
# ◦ Usa la método split().
# ◦ Usa método partition()
# Crea lista que contenga como elementos varias palabras y partir de ella crear una 
#cadena de caracteres que contenga las palabras separadas por guiones.

cadena = "La mujer que esta a mi derecha esta loca"
lista1 = cadena.split(" ")
print(lista1)

lista2 = cadena.partition(" ")
print(lista2)

cadena2 = "_".join(lista1)
print(cadena2)