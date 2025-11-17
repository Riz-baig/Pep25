# Escribe un programa en Python que realice las siguientes operaciones con listas.
# Crear una lista con dos elementos que a su vez sean una lista con los 100 primeros 
# números pares y otra lista con los 100 primeros números impares.
# ◦ Usa un for para crearla.
# ◦ Usa compresión de listas para crearla.
# Recorre la lista y muestra por pantalla todos sus elementos: en una línea todos los 
# números pares y en otra los impares.

lista1 = []
lista2 = []
listaFinal = []

for i in range(0,100): #numero pares con for
    lista1.append(i * 2)

lista2 = [i * 2 + 1 for i in range(100)] #nuemros impares con compresión

listaFinal = [lista1, lista2]

print(lista1, "\n", lista2)

