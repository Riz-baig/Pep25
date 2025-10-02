# Escribe un programa que muestre una lista de números del 1 al 10. Resuelve el ejercicio 
#de dos formas distintas, utilizando los bucles for y while. Cuando utilices el bucle for 
#puedes hacer uso de la función range.
print("Lista con for:")
for i in range(1, 11):  # range(1, 11) genera números del 1 al 10
    print(i)

print("Lista con while:")
i = 1
while i <= 10:
    print(i)
    i += 1

# Escribe un que lea por teclado un número comprendido entre 1 y 10. No se dejara de 
#pedir el número hasta que no se introduzca correctamente.
num = 0
print('introduce numero de 1 a 10 ')
while num < 1 and num > 10:
    numero = int(input("numero introducido no correcto"))
print('Nuemro correcto. ADIOS ')

#Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el 
#ejercicio de 4 formas diferentes. Usando los bucles for y while sin y con la sentencia 
#continue.
#PRIMERA FORMA
print("Con for sin continue:")
for i in range(0, 11):
    if i % 2 == 0:
        print(i)
#SEGUNDA FORMA
print("Con for con continue:")
for i in range(0, 11):
    if i % 2 != 0:   # si es impar, saltamos
        continue
    print(i)
#TERCERA FORMA
print("Con while sin continue:")
i = 0
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1
#CUARTA FORMA
print("Con while con continue:")
i = 0
while i <= 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)


