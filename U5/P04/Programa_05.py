import json
from os import strerror

# leer archivo
try:
    # Abro el archivo en modo lectura
    with open("Paises.json", "r", encoding="utf-8") as fichero:
        # convierto en una lista
        lista = json.load(fichero)
        continente = input("Introduce el nombre del continente: ")

        seleccionados = []  # creo un array vacío
   
        for pais in lista:# recorro la lista
            if pais["continente"].lower() == continente.lower():
                seleccionados.append(pais)  # añade al final de la lista

    if seleccionados:  # si seleccionados no está vacío
        print("Países encontrados:")
        for pais in seleccionados:
            print("- " + pais["nombre"] + " (" + pais["continente"] + ")")
    else:
        print("No se encontraron países en ese continente.")

    # Guardar resultados en paises_filtrados.json
    with open("paises_filtrados.json", "w", encoding="utf-8") as fichero2:
        json.dump(seleccionados, fichero2, ensure_ascii=False, indent=4)

    print("\nArchivo 'paises_filtrados.json' creado correctamente.")

except Exception as exe:
    print("Error:", strerror(exe.errno))
