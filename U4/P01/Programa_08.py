#Declara una cadena "programacion en python".
#Busca la posición de "python" con find() o index().
#Cuenta cuántas veces aparece la letra "o".
#Verifica si comienza por "pro" y termina por "on".

cadena1 ="programacion en python"
num1 = cadena1.find("python")
num2 = cadena1.index("python")

print(num1, " ", num2)
print("las veces que parece letra o: ", cadena1.count("o"))
print(cadena1.startswith("pro") and cadena1.endswith("on"))#devuelve un booleano