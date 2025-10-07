#Escribe un programa que simule un juego en el que dos jugadores tiran dos dados. El que 
#saque mayor puntuación total, gana. Si la puntuación total coincide, gana quien haya 
#sacado el dado con el valor más alto. Si el valor más alto también coincide, empatan.
#Puedes pedir el valor de cada tirada de dados por teclado o usar la  la función 
#random.randrange(1, 7) para obtener un número aleatorio entre 1 y 6 (para ello 
#debes poner import random al inicio del programa)
import random

dado1_j1 = random.randrange(1, 7)
dado2_j1 = random.randrange(1, 7)
total_j1 = dado1_j1 + dado2_j1

dado1_j2 = random.randrange(1, 7)
dado2_j2 = random.randrange(1, 7)
total_j2 = dado1_j2 + dado2_j2

print("Jugador 1: ", dado1_j1, "y", dado2_j1, "Total = ", total_j1)
print("Jugador 2: ", dado1_j2, "y", dado2_j2, "Total = ", total_j2)

if total_j1 > total_j2:
    print("Gana el Jugador 1")
elif total_j2 > total_j1:
    print("Gana el Jugador 2")
else:
    max_j1 = max(dado1_j1, dado2_j1)
    max_j2 = max(dado1_j2, dado2_j2)
    
    if max_j1 > max_j2:
        print("Gana el Jugador 1 (por dado más alto)")
    elif max_j2 > max_j1:
        print("Gana el Jugador 2 (por dado más alto)")
    else:
        print("Empate total, Bien jugado")

#Programa 9, Pedra, Papel o Tijera
print("Juego: Piedra, Papel o Tijera")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")

opcion_usuario = int(input("Seleccione una opción (1, 2 o 3): "))
opcion_pc = random.randint(1, 3)

opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}

print("Tú elegiste:", opciones.get(opcion_usuario, "Desconocido"))
print("La máquina eligió:", opciones[opcion_pc])

if opcion_usuario == opcion_pc:
    print("Empate")
elif (opcion_usuario == 1 and opcion_pc == 3) or \
     (opcion_usuario == 2 and opcion_pc == 1) or \
     (opcion_usuario == 3 and opcion_pc == 2):
    print("¡Has ganado!")
else:
    print("Has perdido")

