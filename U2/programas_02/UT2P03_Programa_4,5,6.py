
#Escribe un programa que use un bucle while y le pida continuamente al usuario que 
#introduzca un número hasta que ingrese 45 como la número de salida secreto, en cuyo 
#caso el mensaje "¡Has dejado el bucle con éxito" debe imprimirse en la pantalla y el bucle 
#debe terminar.
#CONTROLADO CON WHILE
n1 = 45
n = 0
while n != n1:
    n = int(input("introduce el numero para salir del bucle: "))
print("Has salido del bucle con exito")
#CONTROLADO CON WHILE
n1 = 45
while True:
    n = int(input("Introduce el número para salir del bucle: "))
    if n == n1:
        break
print("Has salido del bucle con éxito")

#Escribe un programa que pida un número y muestre una lista de números desde 1 al 
#número. Se debe controlar que el número no se menor que 1 ni mayor que 10, si es así se 
#pedirá que si introduzca de nuevo, y así hasta que se introduzca el número correcto
num = -1
while num < 0 and num > 10:
    num = int(input("introduce un numero de 1 a 10 "))

for i in range(num):
    print(i)

#Escribe un programa  que realice las siguientes operaciones:
 #• Leer por teclado un número comprendido entre 1 y 10. Se vuelve a pedir hasta que 
#no se introduzca el número correcto.
# • Una vez que ha leído el número se tiene que mostrar su tabla de multiplicar.
# • Después de mostrar la tabla de multiplicar se tiene que preguntar al usuario si 
#desea introducir otro número o no. Si el usuario selecciona que quiere continuar el 
#programa tendrá que volver a ejecutarse y repetir los mismos pasos. Si el usuario 
#indica que no quiere continuar el programa finaliza.

num = -1
seguir = True
opcion = -1

while seguir:
    while num < 1 or num > 10:
        num = int(input("introduce el numero correcto: "))
    print("has introducido el numero correcto. ")

    for i in range(1,11):
        print(num, " X ", i, " = ", num*i)
    num = -1
    opcion = int(input("si deseas continuar pulsa 1, para salir pulsa 0: "))
    if opcion == 0:
        seguir = False
print("Hasta Pronto")


