# Escribe un programa en Python que realice las siguientes operaciones con listas partiendo del programa anterior.
# Elimina el cuarto elemento de la lista utilizando la instrucción del.
# Elimina un elemento de la lista utilizando el método remove().
# Verifica si un un elemento pertenece a la lista.
# Muestra por pantalla el índice de un elemento de la lista.
# Muestra por pantalla el número de ocurrencias de un elemento en la lista.

mi_lista25 = ["nombre", 45, True, 25.50]

print("la longitud de la lista: " , len(mi_lista25))
print("La posicion 0 de lista: " , mi_lista25[0])
print("el ultimo valor de la lista: " , mi_lista25[-1])

mi_lista25[2] = "Apellido"
mi_lista25.append("añadido_final")
mi_lista25.insert(1, "insertado")
print("lista compeleta: ", mi_lista25)

del mi_lista25[4] # borra el cuarto elemento de la lista
print("Borrado el cuarto elemento de la lista con del: ", mi_lista25)

mi_lista25.remove(mi_lista25[1])
print("Borrado un elemento de la lista con remove: ", mi_lista25)

print("nombre" in mi_lista25)

print(mi_lista25.index("nombre"))

print(len(mi_lista25))