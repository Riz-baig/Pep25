# Escribe un programa en Python que realice las siguientes operaciones con listas.

# Crea una lista que contenga 30 veces la palabra “Vacío”
# Crear una lista que contenga los 10 primeros números pares.

palabra = "Vacio "
lista = palabra * 30
lista1 = [] #creo lista vacia

for i in range(0, 10):
    lista1.append(i*2) #genera numero par al final de la lista1


print(lista)
print(lista1)


