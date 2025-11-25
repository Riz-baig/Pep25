import json

cadena_json = '''
[
  {"nombre": "Chile", "moneda": "Peso chileno"},
  {"nombre": "Egipto", "moneda": "Libra egipcia"}
]
'''

lista = json.loads(cadena_json)# Converto la cadena JSON a un objeto Python

print("Tipo de dato:", type(lista))# Muestro el tipo de dato obtenido

# Imprimo cada país con su moneda
for pais in lista:
    print(f"{pais['nombre']} usa la moneda {pais['moneda']}.")

