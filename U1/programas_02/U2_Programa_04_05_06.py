
print ("Ejercicio 04")
print ("")
#Escribe un programa que pregunte la base y altura de una rectángulo y calcule su área y perímetro.
Base = int(input("indicame la base de rectangulo: "))
altura = int(input("Indicame la altura del triangulo: "))
area = Base * altura
print("el area del rectánglo es: ", area)

print ("Ejercicio 05")
print ("")
#Escribe un programa que pregunte al usuario dos números y calcule su suma, resta, 
#multiplicación, división, módulo y potencia

num1 = int(input("Dime el primer numero: "))
num2 = int(input("Dime el segundo numero: "))
print ("La suma de los dos es ", num1 + num2)
print ("La resta de los dos es ", num1 - num2)
print ("La multiplicación de los dos es ", num1 * num2)
print ("La división de los dos es ", num1 / num2)
print ("La modulo de los dos es ", num1 % num2)
print ("La potencia de los dos es ", num1 ** num2)

print ("Ejercicio 05")
print ("")
# Escribe un programa que convierta un valor dado en grados Fahrenheit a grados Celsius

num1 = float(input("introduce el valor en Fahrenheit: "))
print ("El valor convertido en celcius es: ", (num1 - 32) * 5 / 9)