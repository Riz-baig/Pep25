# Escribe un programa en Python que realice las siguientes operaciones con listas.
# Crea una lista solo de números (ejemplo: temperaturas =). 
# Calcula la suma de todos los elementos utilizando la función sum() y la media 
# (promedio) combinando sum() y len().
# Muestra los valores máximo y mínimo de la lista.

cantidad = 1,2,3,4,5,6,7,8,9

suma = sum(cantidad)
promedio = (suma / len(cantidad))

print("Suma de los elementos: ",suma)
print("Promedio: ",promedio)
print("Valor máximo: ", max(cantidad))
print("Valor minimo: ", min(cantidad))