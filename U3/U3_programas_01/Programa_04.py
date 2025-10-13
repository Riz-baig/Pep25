import math

def mostrar_menu():
    print("Elige una opción:")
    print("1. Calcular el área de un círculo.")
    print("2. Calcular el área de un triángulo.")
    print("3. Calcular el área de un rectángulo.")
    print("4. Salir")

def main():
    opcion = 0
    while opcion != 4: 
        mostrar_menu()
        opcion = int(input("Introduce una opción (1-4): "))
        if opcion == 1:
            opcion1()
        elif opcion == 2:
            opcion2()
        elif opcion == 3:
            opcion3()
        elif opcion == 4:
            print("Saliendo del programa...")
        else:
            print("Opción no válida.")

def opcion1(): # opción 1 para círculo
    radio = -1
    while radio <= 0:
        radio = float(input("Introduce el radio del círculo: "))
        if radio <= 0:
            print("El radio debe ser mayor que 0.")
    calcular_area_circulo(radio)

def opcion2(): # opción 2 para triángulo
    base = -1
    altura = -1
    while base <= 0:
        base = float(input("Introduce la base del triángulo: "))
        if base <= 0:
            print("La base debe ser mayor que 0.")
    while altura <= 0:
        altura = float(input("Introduce la altura del triángulo: "))
        if altura <= 0:
            print("La altura debe ser mayor que 0.")
    calcular_area_triangulo(base, altura)

def opcion3(): # opción 3 para rectángulo
    base = -1
    altura = -1
    while base <= 0:
        base = float(input("Introduce la base del rectángulo: "))
        if base <= 0:
            print("La base debe ser mayor que 0.")
    while altura <= 0:
        altura = float(input("Introduce la altura del rectángulo: "))
        if altura <= 0:
            print("La altura debe ser mayor que 0.")
    calcular_area_rectangulo(base, altura)

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    print("El área del círculo es:", area)

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    print("El área del triángulo es:", area)

def calcular_area_rectangulo(base, altura):
    area = base * altura
    print("El área del rectángulo es:", area)

main()#invoca a enu main
