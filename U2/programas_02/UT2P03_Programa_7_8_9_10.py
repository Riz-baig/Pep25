#Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la 
#suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza 
#la instrucción break y otra no.
#sin break
import random


num = -1
suma = 0
conta = 0
while num != 0:
    num = int(input("Introduce nuvamente el numero, si pulsas 0, terminara el programa: "))
    suma = suma + num
    conta = conta + 1
print("La suma total de tus numero es: ", suma)
print("La media de todos los numeros introducidos es: ", suma/conta)
#con break
suma = 0
conta = 0
while True:
    num = int(input("Introduce nuevamente el número (0 para terminar): "))
    if num == 0:
        break
    suma += num
    conta += 1
print("La suma total de tus números es:", suma)
print("La media de todos los números introducidos es:", suma / conta)

#Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación 
#solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va 
#respondiendo si el número a adivinar es mayor o menor que el introducido. El programa 
#termina cuando se acierta el número.
#Puedes generar el número usando la función random.randrange(1, 21) para 
#obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio 
#del programa).
#Mejora el programa de forma que el usuario tenga solo 3 intentos.

num = random.randrange(1, 21)
adivina = 0
intentos = 0
while num != adivina and intentos < 3:
    adivina = int(input("Introduce el numero: "))
    if num < adivina:
        print("tu numero es mayor que el mio.")
        intentos = intentos + 1
    elif num > adivina:
        print("tu numero es menor que el mio")
        intentos = intentos + 1
    else:
        print("Has adivinado")
        print("has gastado ", intentos, " intentos.")

#Escribe un programa para jugar a una versión muy simplificada del black jack. En primer 
#lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A 
#continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando 
#para obtener su puntuación,  hasta que el quiera. Si se pasa de 21 pierde, si obtiene una 
#puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la 
#banca gana.

banca = random.randint(17, 21)
print("La banca ya tiene su jugada.")
puntuacion_jugador = 0
seguir_jugando = 's'

while puntuacion_jugador <= 21 and seguir_jugando == 's':
    carta = random.randint(1, 5)
    print(f"Has sacado una carta de valor: {carta}")
    puntuacion_jugador += carta
    print(f"Puntuación actual: {puntuacion_jugador}")
    
    if puntuacion_jugador <= 21:
        seguir_jugando = input("¿Quieres sacar otra carta? (s/n): ").lower()

if puntuacion_jugador > 21:
    print("Te has pasado de 21. ¡Has perdido!")
else:
    print(f"\nLa banca tenía: {banca}")
    print(f"Tu puntuación final: {puntuacion_jugador}")
    
    if puntuacion_jugador > banca:
        print("¡Has ganado!")
    else:
        print("Has perdido. Tu puntuación no supera la de la banca.")

#Modifica el programa anterior par que pida en primer lugar el número de jugadores que 
#van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la 
#banca.


# Número de jugadores
num_jugadores = int(input("¿Cuántos jugadores van a jugar? "))

# La banca hace su jugada
banca = random.randint(17, 21)
print("\nLa banca ya tiene su jugada (entre 17 y 21).")

# Turno de cada jugador
for jugador in range(1, num_jugadores + 1):
    print(f"\n--- Turno del jugador {jugador} ---")
    puntuacion_jugador = 0
    seguir_jugando = 's'

    while puntuacion_jugador <= 21 and seguir_jugando == 's':
        carta = random.randint(1, 5)
        print(f"Has sacado una carta de valor: {carta}")
        puntuacion_jugador += carta
        print(f"Puntuación actual: {puntuacion_jugador}")
        
        if puntuacion_jugador <= 21:
            seguir_jugando = input("¿Quieres sacar otra carta? (s/n): ").lower()

    # Resultado del jugador
    if puntuacion_jugador > 21:
        print("Te has pasado de 21. ¡Has perdido!")
    else:
        print(f"\nLa banca tenía: {banca}")
        print(f"Tu puntuación final: {puntuacion_jugador}")
        
        if puntuacion_jugador > banca:
            print("¡Has ganado!")
        else:
            print("Has perdido. Tu puntuación no supera la de la banca.")





