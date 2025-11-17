# Escribe un programa en Python que realice las siguientes operaciones con listas 
# partiendo del programa anterior.
# > Crea una nueva lista extrayendo un slice de los elementos desde el índice 2 hasta 
# el índice 5 (recuerda que el índice final es excluido).
# > Muestra una nueva lista que contenga solo los elementos de tu lista original que 
# estén en posiciones pares, utilizando un incremento de 2 en el slicing. 
# > Reverso
# ◦ Crear nueva lista en orden inverso utilizando la sintaxis de slicing [::-1].
# ◦ Usa el método reverse() para invertir la lista y modificar su contenido.

mi_lista25 = ["nombre", 45, True, 25.50]

print("la longitud de la lista: " , len(mi_lista25))
print("La posicion 0 de lista: " , mi_lista25[0])
print("el ultimo valor de la lista: " , mi_lista25[-1])

mi_lista25[2] = "Apellido"
mi_lista25.append("añadido_final")
mi_lista25.insert(1, "insertado")
print("lista compeleta: ", mi_lista25)

mi_lista2 = mi_lista25[slice(2,5)] #slice(2, 5) recoge la parte desde indice 2 a5 de mi_lista25
print(mi_lista2)

lista_par = mi_lista25[slice(0, len(mi_lista25), 2)] #slice(posicion inicial, posicion final, numero de saltos)
print("Lista de elementos par: ", lista_par)

lista_reverso = mi_lista25[slice(len(mi_lista25),0 ,-2)]
print("lista inversa con salto de dos: ", lista_reverso)

lista_Inversa = mi_lista25[::-1] #invierte la lista
print("Lista inversa con slicing: ", lista_Inversa)

mi_lista25.reverse()
lista_reve = mi_lista25
print("Lista reversa con reverse: ",lista_reve)


