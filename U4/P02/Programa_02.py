#Escribe un programa en Python que lea por teclado una cadena y un carácter, y 
#reemplace todos los dígitos en la cadena por el carácter. Ej: su clave es: 1540 y X debería 
#devolver su clave es: XXXX

cadena = "estoy aburrido"
caracter = "o"
cadena1 = ""

for c in cadena:
    if(c != " "):
        c = "X"
    cadena1 += c
print (cadena1)
