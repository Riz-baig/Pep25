#Escribe un programa que pida primero un número par y luego un número impar (positivos 
#o negativos). En caso de que uno o los dos valores no sea correcto (es decir no sea par o 
#impar respectivamente), se mostrará un aviso.

num1 = int(input("Introduce un número par: "))
num2 = int(input("Introduce un número impar: "))

while not (num1 % 2 == 0 and num2 % 2 != 0):
    print("algo na has hecho bien, primero par y luego impaaarrr")
    num1 = int(input("Introduce un número par: "))
    num2 = int(input("Introduce un número impar: "))

print("Ahpora si, ADIOS")

#Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no 
#es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o 
#negativo) y si el valor no es correcto, mostrará un aviso
# Pedir un número par
num1 = int(input("Introduce un número par (positivo o negativo): "))

if num1 % 2 == 0:
    num2 = int(input("Introduce un número impar (positivo o negativo): "))
    if num2 % 2 != 0:
        print("Muy bien, los números son correctos.")
    else:
        print("El segundo número no es impar.")
else:
    print("El primer número no es par.")

#Escribe un programa que pida dos numero y muestre su división. Se deben tener en 
#cuenta que no se puede dividir por 0 mostrando en ese caso un aviso.
num1 = int(input("introduce el dividendo: "))
num2 = int(input("introduce el divisor: "))
if num2 == 0:
    print("el divisor no puede ser 0. Adios")
else:
    print("el resultado es: ", num1/num2) #el resulta puede ser un numero real

#Escribe un programa  que lea por teclado un número real entre 1 y 10, simulando una 
#nota numérica, y muestre un mensaje indicando la calificación obtenida teniendo en 
#cuenta los siguientes rangos:
#• Insuficiente: [0, 5)
#• Suficiente: [5, 6)
#• Bien: [6, 7)
#• Notable: [7, 9)
#• Sobresaliente: [9, 10]
#Si el número introducido no está en ninguno de los rangos anteriores debe mostrar un 
#mensaje de error indicando que la nota no es válida.
#Hay que usar la estructura match.

num1 = int(input("introduce la nota y te digo la calificación: "))
match num1:
    case 1|2|3|4:
        print("Insuficiente")
    case 5|6:
        print("Suficiente")
    case 7:
        print("Bien")
    case 8|9:
        print("Notable")
    case 10:
        print("Sobresaliente")
    case _:
        print("Nota no válida (introduce entre 1 y 10)")
        


