from matematicas.operaciones import suma, resta, multiplicar, dividir
from matematicas.figuras import area_rectangulo, area_triangulo, area_circulo

def main():
    def menu():
        print("1. Operaciones matemáticas")
        print("2. Cálculo de áreas geométricas")
        print("3. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            ope1 = float(input("Introduce el primer número: "))
            ope2 = float(input("Introduce el segundo número: "))
            operacion = int(input("Pulsa 1 para suma, 2 para resta, 3 para multiplicación o 4 para dividir: "))

            if operacion == 1:
                print("Suma:", suma(ope1, ope2))
            elif operacion == 2:
                print("Resta:", resta(ope1, ope2))
            elif operacion == 3:
                print("Multiplicación:", multiplicar(ope1, ope2))
            elif operacion == 4:
                print("División:", dividir(ope1, ope2))
            else:
                print("Opción no válida.")

        elif opcion == 2:
            print("1. Área del rectángulo")
            print("2. Área del triángulo")
            print("3. Área del círculo")
            fig = int(input("Elige una figura: "))

            if fig == 1:
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                print("Área del rectángulo:", area_rectangulo(base, altura))
            elif fig == 2:
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                print("Área del triángulo:", area_triangulo(base, altura))
            elif fig == 3:
                radio = float(input("Radio: "))
                print("Área del círculo:", area_circulo(radio))
            else:
                print("Opción no válida.")

        elif opcion == 3:
            print("¡Hasta luego!")
            return False
        else:
            print("Opción no válida.")
        return True

    while menu():
        pass

main()


            