import platform
import os

print("Procesador:", platform.processor())
print("Sistema operativo y versión:", platform.system(), platform.version())
print("Nombre del host:", platform.node())
print("Directorio actual:", os.getcwd())