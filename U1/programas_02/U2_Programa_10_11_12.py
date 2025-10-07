#Escribe un programa que dado un número de dos cifras, diseñe un algoritmo que permita 
#obtener el número invertido.
numero = int(input("Introduce un número de dos cifras: "))

if 10 <= numero <= 99:
    decenas = numero // 10       # obtenemos la primera cifra
    unidades = numero % 10       # obtenemos la segunda cifra
    invertido = unidades * 10 + decenas
    print("El número invertido es:", invertido)
else:
    print("Error: el número no tiene dos cifras.")


#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.  El tiempo 
#de viaje hasta llegar a otra ciudad B es de N segundos. Escribie un programa que 
#determine la hora de llegada a la ciudad B
HH = int(input("Hora de salida (HH): "))
MM = int(input("Minutos de salida (MM): "))
SS = int(input("Segundos de salida (SS): "))
N = int(input("Duración del viaje en segundos: "))

segundos_salida = HH * 3600 + MM * 60 + SS
segundos_llegada = segundos_salida + N
segundos_llegada = segundos_llegada % 86400  # 86400 = 24h en segundos

hora = segundos_llegada // 3600
minutos = (segundos_llegada % 3600) // 60
segundos = segundos_llegada % 60

print(f"Hora de llegada: {hora:02d}:{minutos:02d}:{segundos:02d}")

#Sabiendo que 1 milla equivale a 1,61 Km escribe un programa que pida un número de 
#millas y un número de Km, muestre respectivamente el número de millas y kilómetros. Los 
#resultados deben estar redondeados a 2 decimales

MILLA_A_KM = 1.61

millas = float(input("Introduce un número de millas: "))
km = float(input("Introduce un número de kilómetros: "))

millas_a_km = millas * MILLA_A_KM
km_a_millas = km / MILLA_A_KM

print(f"{millas} millas equivalen a {millas_a_km:.2f} km")
print(f"{km} kilómetros equivalen a {km_a_millas:.2f} millas")

