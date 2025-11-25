from os import strerror
import json
paises = [
    {"nombre": "Japón", "continente": "Asia", "poblacion": 125.7},
    {"nombre": "Canadá", "continente": "América", "poblacion": 38.2},
    {"nombre": "España", "continente": "Europa", "poblacion": 48.0}
]

try:
    
    with open("Paises.json", "w", encoding="utf-8") as fichero:#Abro el archivo en modo escritura
        fichero.write(json.dumps(paises, ensure_ascii=False))#escribo en archivo jason.dump hace escribir en formato json
except Exception as exe:
    print("Error:", strerror(exe.errno))

#leer archivo
try:
    # Abro el archivo en modo lectura
    with open("Paises.json", "r", encoding="utf-8") as fichero:
        # concvierto en una lista
        lista = json.load(fichero)

        # Recorre la lista
        for pais in lista:
            print(f"{pais['nombre']} está en {pais['continente']} y tiene {pais['poblacion']} millones de habitantes.")

except Exception as exe:
    print("Error:", strerror(exe.errno))

