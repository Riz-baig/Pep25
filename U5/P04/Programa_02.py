from os import strerror
import json
capitales = [
  {"país": "Francia", "capital": "París"},
  {"país": "Australia", "capital": "Canberra"},
  {"país": "Kenia", "capital": "Nairobi"},
  {"país": "Brasil", "capital": "Brasilia"}
 ]

try:
    
    with open("capitales.json", "w", encoding="utf-8") as fichero:#Abro el archivo en modo escritura
        fichero.write(json.dumps(capitales, ensure_ascii=False, indent=4))#escribo en archivo jason.dump hace escribir en formato json
        print("Archivo 'capitales.json' creado correctamente.")
except Exception as exe:
    print("Error:", strerror(exe.errno))
