# Escribe un programa en Python que lea por teclado números y los guare en una lista, el 
# proceso finaliza cuando se introduzca un número negativo.  A continuación que muestre el 
# máximo de los números guardado en la lista  y  los números pares de la lista.

lista = []
num = 0

while num >= 0:
    num = int(input("Introduce el numero, no negativo: "))
    if (num >= 0):
        lista.append(num)

print(lista)