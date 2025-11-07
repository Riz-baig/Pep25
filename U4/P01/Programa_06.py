#Crea una cadena "Python".
#Extrae la subcadena "Pyt" con slicing.
#Extrae los caracteres en posiciones pares con slicing ::2.
#Invierte la cadena con slicing [::-1].
#Recorre la cadena carácter por carácter e imprímelos.

cadena1 = "Python"
cadena2 = cadena1[0:3] #corta la cadena desde 0 hasta 3
print (cadena2)

cadena3 = cadena1[::2] #extrae solo las posiciones pares
print(cadena3)

cadena4 = cadena1[::-1] #invierte la cadena
print(cadena4)

for c in cadena1: #recorre caracter por caracter
    print(c)