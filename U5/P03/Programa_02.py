# Crea un programa que lea el archivo ciudades.csv usando csv.DictReader().
# Debe:
# - Mostrar los nombres de las columnas (fieldnames).
# - Recorrer las filas e imprimir información como:
# {Ciudad} ({País}) tiene una población aproximada de {Población 
# (millones)} millones.

# Si el archivo no incluye cabecera, define manualmente los campos necesarios

import csv
from os import strerror

try:
    # Abrir el fichero
    with open("ciudades.csv", "r", encoding="utf-8") as fichero:
        lector = csv.DictReader(fichero) #DictReader converte cada fila en un diccionrio

        print("Columnas encontradas:", lector.fieldnames, "\n")

        # Recorrer las filas
        for fila in lector:
            ciudad = fila["Ciudad"]
            pais = fila["País"]
            poblacion = fila["Población (millones)"]

            print(f"{ciudad} ({pais}) tiene una población aproximada de {poblacion} millones.")

except Exception as e:
    print("Error:", strerror(e.errno))

