# Ordenación Modificable vs. no modificable:
# ◦ Crea una lista de cadenas no ordenadas. Utiliza el método sort() para 
# ordenar la lista y comprueba que la lista original ha sido modificada.
# ◦ Utiliza la función sorted() y comprueba que la lista original no se modifica.
# Concatenación
#  ◦ Crea dos listas y crea una nueva lista que se la concatenación de las anteriores.
#  ◦ Crea dos listas y amplia la primera añadiendo los elementos de las segunda 
# Diferencia de copia:
#  ◦ Asigna tu lista original a una nueva variable utilizando una asignación directa 
# (copia = lista). Muestra los identificadores de memoria de ambas variables 
# usando id() para verificar que apuntan al mismo objeto.

lista = ["Cinco", "Tres", "Siete", "Ambar", "Base", "Farmacia", "Linares", "Zamora", "Rizwan"]
lista_2= ["Said", "Elia", "Samuel", "Wentin"]
lista_3 = lista + lista_2
copia = lista

#esto modifica la lista
#lista.sort()

print(sorted(lista)) #solo ordena temporalmente, no modifica original

print(lista)
print(lista_3)

print(id(copia))
print(id(lista))

