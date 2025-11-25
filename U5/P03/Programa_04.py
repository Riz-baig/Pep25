# Crea un programa que escriba un archivo patrimonios.csv con información sobre 
# ciudades con lugares Patrimonio de la Humanidad:
# patrimonios = [
#    {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
#    {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
#    {"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"}]
# El programa debe:

# Usar DictWriter con fieldnames=["Ciudad", "País", "Lugar emblemático"].
# Escribir la cabecera con writeheader() y las filas con writerows().
# Cambiar el delimitador a ;.
# Mostrar un mensaje final: "Archivo 'patrimonios.csv' generado correctamente."

import csv
from os import strerror

patrimonios = [
    {"Ciudad": "Roma",   "País": "Italia", "Lugar emblemático": "Coliseo"},
    {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
    {"Ciudad": "Kioto",  "País": "Japón",  "Lugar emblemático": "Templos históricos"}
]

try:
    with open("patrimonios.csv", "w", encoding="utf-8", newline="") as fichero:
        
        cabecera = ["Ciudad", "País", "Lugar emblemático"] #defino las columnas

        # Crea el escritor DictWriter con delimitador ;
        escritor = csv.DictWriter(fichero, fieldnames=cabecera, delimiter=';')

        escritor.writeheader()# Escribe cabecera
 
        escritor.writerows(patrimonios)# Escribe todas las filas

    print("Archivo 'patrimonios.csv' generado correctamente.")

except Exception as e:
    print("Error:", strerror(e.errno))
