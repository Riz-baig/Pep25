# Escribe un programa en Python que realice las siguientes operaciones con listas 
# partiendo el programa anterior:
# Partiendo de mi_listaXX del ejercicio anterior modifica el valor del tercer elemento a 
# un nuevo valor de tu elección.
# Añade un nuevo elemento al final de la lista utilizando el método append().
# Inserta una nueva cadena de caracteres en la segunda posición de la lista (índice 
# 1) utilizando el método insert().
# Recorre la lista y muestra sus elementos por pantalla.

mi_lista25 = ["nombre", 45, True, 25.50]

print(len(mi_lista25))
print(mi_lista25[0])
print(mi_lista25[-1])

mi_lista25[2] = "Apellido"
mi_lista25.append("añadido_final")
mi_lista25.insert(1, "insertado")

print(mi_lista25)



