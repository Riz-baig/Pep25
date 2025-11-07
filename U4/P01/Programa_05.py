
# Declara dos cadenas y únelas con concatenación (+).
# Repite una cadena tres veces con *.
# Compara dos cadenas lexicográficamente e indica cuál es mayor.
# Comprueba si una subcadena pertenece a otra con in.

cadena1 = "estan dando un discurso, "
cadena2 = "y esta bastante aburrido"
cadenaunida = cadena1+cadena2

print(f"la cadena unida es: {cadenaunida}")

print ("repetida tres veces: " + cadena1 * 3)

if (cadena1 > cadena2):
    print(cadena1 + "// es mayor que //" + cadena2)
elif (cadena2 > cadena1):
    print(cadena2 + "// es mayor que //" + cadena1)
else:
    print("las cadenas son iguales.")


print(cadena1 in cadena2) #esto va imprimir false por que son dos cadenas totalmente distintas
print(cadena1 in cadenaunida)#imprime true, porque si que esta dentro
print("estan" in cadena1) #cumprueba la palabra "estan" en cadena1