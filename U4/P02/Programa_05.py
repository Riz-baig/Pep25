# Mejora las funciones anteriores de cifrado y descifrado con los siguientes cambios.
# • El cifrado César original cambia cada carácter por otro: a se convierte en b, z se 
# convierte en a, y así sucesivamente (por defecto el valor desplazado es 1).  Ahora 
# la idea es hacerlo un poco más difícil y permitir que el valor desplazado provenga 
# del rango 1 – 25 (si  valor de desplazado es 3, la A se cambiará por la D). 
#• Además, deja que el código conserve las mayúsculas y minúsculas (las minúsculas 
# permanecerán en minúsculas) y todos los caracteres no alfabéticos deben 
# permanecer intactos.
# Escribe un programa que:
# • Le pida al usuario una línea de texto para cifrar..
# • Le pida al usuario un valor de cambio (un número entero del rango 1..25, nota: 
# debes validar la entrada para asegurarnos que el número está dentro del rango).
# • Imprima el texto cifrado.
import string

cadena = input("introduce la cadena: ") #para convertir en mayusculas
cifrado = ""
lista_maysculas = list(string.ascii_uppercase)
lista_minusculas = list(string.ascii_lowercase)

salto = -1
def validar(salto):
    while(salto > 25 or salto < 1):
        salto = int(input("introduce el salto: "))
    return salto


def cifrar(cadena, salto, cifrado,lista_maysculas, lista_minusculas ):

    for letra in cadena:

        if letra in lista_maysculas:
            index = ((lista_maysculas.index(letra))+ salto) % 26 #esto hace que de z pase a A y calcule el salto
            cifrado += lista_maysculas[index]

        elif (letra in lista_minusculas):
            index = ((lista_minusculas.index(letra))+ salto) % 26
            cifrado += lista_minusculas[index]

        else:
            cifrado += letra
    print (cifrado)

validar(salto)
cifrar(cadena, salto, cifrado,lista_maysculas, lista_minusculas)