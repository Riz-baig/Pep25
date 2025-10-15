import math

def main():
    print("¿Qué operación matemática quieres hacer?")
    print("1. Seno de un ángulo")
    print("2. Coseno de un ángulo")
    print("3. Raíz cuadrada de un número")
    print("4. Potencia de dos números")

    opcion = int(input("Introduce la opción (1-4): "))

    if opcion == 1:
        angulo = float(input("Introduce el ángulo en grados: "))
        print("El seno de", angulo, "grados es:", math.sin(math.radians(angulo)))

    elif opcion == 2:
        angulo = float(input("Introduce el ángulo en grados: "))
        print("El coseno de", angulo, "grados es:", math.cos(math.radians(angulo)))

    elif opcion == 3:
        numero = float(input("Introduce el número: "))
        if numero < 0:
            print("No se puede calcular la raíz cuadrada de un número negativo.")
        else:
            print("La raíz cuadrada de", numero, "es:", math.sqrt(numero))

    elif opcion == 4:
        base = float(input("Introduce la base: "))
        exponente = float(input("Introduce el exponente: "))
        print(base, "elevado a", exponente, "es:", math.pow(base, exponente))

    else:
        print("Opción no válida.")

main()
