#Usando uno de los operadores de comparación en Python, escribe un programa simple de 
#dos líneas que tome el parámetro n como entrada, que es un entero, e imprima False si n 
#es menor que 100, y True si n es mayor o igual que 100. No debes crear ningún bloque if.
n = int(input("Introduce un número: "))
print(n >= 100)



#Escribe un programa que reciba un número de bytes y muestre por pantalla cuantos 
#GBytes, MBytes, KBytes y Bytes son. Tanto para el sistema decimal como el binario
bytes_input = int(input("Introduce el número de bytes: "))

GB_si = bytes_input // (1000**3)
MB_si = (bytes_input % (1000**3)) // (1000**2)
KB_si = (bytes_input % (1000**2)) // 1000
B_si  = bytes_input % 1000

GiB = bytes_input // (1024**3)
MiB = (bytes_input % (1024**3)) // (1024**2)
KiB = (bytes_input % (1024**2)) // 1024
B_iec = bytes_input % 1024

print(f"{bytes_input} bytes en sistema decimal (SI): {GB_si} GB, {MB_si} MB, {KB_si} KB, {B_si} bytes")
print(f"{bytes_input} bytes en sistema binario (IEC): {GiB} GiB, {MiB} MiB, {KiB} KiB, {B_iec} bytes")

