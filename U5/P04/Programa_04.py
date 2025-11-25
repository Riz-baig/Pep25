import json

pais = {
  "nombre": "Islandia",
  "capital": "Reikiavik",
  "idiomas": ["Islandés", "Inglés"],
  "superficie_km2": 103000 }

#convierto el diccionario en una cadena
cadena = json.dumps(pais, sort_keys=True, ensure_ascii= False, indent= 2)
print(cadena)