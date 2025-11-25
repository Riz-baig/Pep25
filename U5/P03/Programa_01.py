import csv
from os import strerror
# Crea un fichero llamado ciudades.csv con el siguiente contenido:
# Ciudad,País,Población (millones)
# Tokio,Japón,37.4
# Delhi,India,30.3
# Shanghái,China,27.1
# São Paulo,Brasil,22.0

# Escribe un programa que:
# Lea el fichero usando csv.reader().
# Muestre en pantalla frases como:
# La ciudad de Tokio está en Japón y tiene 37.4 millones de habitantes.
# Controle las posibles excepciones

try:
    # Abro el archivo 
    with open("ciudades.csv", "r", encoding="utf-8") as fichero:
        lista = csv.reader(fichero)

        next(lista)  # Saltamos la cabecera

        # leo cada linea y lo guardo en sus variables
        for fila in lista:
            ciudad = fila[0]
            pais = fila[1]
            poblacion = fila[2]

            print("La ciudad de " + ciudad + " está en " + pais + " y tiene " + poblacion + " millones de habitantes.")

except Exception as e:
    print("Error:", strerror(e.errno))
