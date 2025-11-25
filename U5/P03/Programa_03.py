# Crea un programa que genere un fichero nuevo llamado capitales.csv con los 
# siguientes datos:
# Ciudad     País          Continente
# París      Francia       Europa
# Canberra   Australia     Oceanía
# Nairobi    Kenia         África
# Ottawa     Canadá        América

# El programa debe:
#  Escribir la cabecera y los datos con writerow() y writerows().
# Usar un bloque try/except con os.strerror() para capturar errores de E/S.
# Confirmar con un mensaje final: "Archivo 'capitales.csv' creado correctamente."

import csv
from os import strerror

# lista de capitales
capitales = [["París",    "Francia",   "Europa"],
             ["Canberra", "Australia", "Oceanía"],
             ["Nairobi",  "Kenia",     "África"],
             ["Ottawa",   "Canadá",    "América"]]

try:
    # Abre el archivo en modo escritura
    with open("capitales.csv", "w", encoding="utf-8", newline="") as fichero:
        escribe = csv.writer(fichero)

        # Escribe la cabecera
        escribe.writerow(["Ciudad", "País", "Continente"])

        # Escribe varias filas
        escribe.writerows(capitales)

    print("Archivo 'capitales.csv' creado correctamente.")

except Exception as e:
    print("Error:", strerror(e.errno))
