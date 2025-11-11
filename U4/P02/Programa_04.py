#Escribe un función en Python que reciba una cadena y retorne otra cadena cifrada usando 
#el cifrado Cesar. Este cifrado fue (probablemente) inventado y utilizado por Cayo Julio 
#César y sus tropas durante las Guerras Galas. La idea es bastante simple: cada letra del 
#mensaje se reemplaza por su consecuente más cercano (A se convierte en B, B se 
#convierte en C, y así sucesivamente). La única excepción es la Z, la cual se convierte en A.
#Partimos de las siguientes condiciones:
#• Solo acepta letras latinas (nota: los Romanos no usaban espacios en blanco ni dígitos).
#• Todas las letras del mensaje están en mayúsculas (nota: los Romanos solo conocían las mayúsculas)
# El código, con este mensaje: AVE CAESAR da como salida: BWF DBFTBS
# Crea otra función que reciba una cadena cifrada y retorne otra descifrada.
# Prueba las dos funciones

import string


cadena = input("introduce la cadena: ")
resultado = ""
lista = list(string.ascii_uppercase) #esto crea un array que tiene todo el abecedario

for letra in cadena:
    if letra == " ":
        resultado += " "
    elif letra == "Z":
        resultado += "A"  # La Z pasa a A
    elif letra in lista:
        # Encontrar el índice y sumar 1
        indice = lista.index(letra)
        resultado += lista[indice + 1]
    else:
        # Si hay un carácter no alfabético
        resultado += letra

print(resultado)


def descifrar(resultado):
    descifrado = ""
    for letra in resultado:
        if letra == " ":
            descifrado += " "
        elif letra == "A":
            descifrado += "Z"  # La Z pasa a A
        elif letra in lista:
            # Encontrar el índice y sumar 1
            indice = lista.index(letra)
            descifrado += lista[indice - 1]
        else:
        # Si hay un carácter no alfabético
            descifrado += letra
    print(descifrado)

descifrar(resultado)