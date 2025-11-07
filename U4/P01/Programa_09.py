#Muestra el código Unicode de un emoji (ord(), hex()).
#Crea un carácter a partir de un código numérico (chr()).
#Imprime los caracteres ASCII del 48 al 57 (dígitos) en una línea.


import sys
sys.stdout.reconfigure(encoding='utf-8') #lo necesito para imprimir emo

emo = "😀"
print ("Emoji: ", emo)
print("ord: ", ord(emo))
print("Hex: ", hex(ord(emo)))

num = 128512
cadena = chr(num)
print(cadena)

print("Caracteres ASCII del 48 al 57 (dígitos):")
for i in range(48, 58):
    print(chr(i), end=" ")
