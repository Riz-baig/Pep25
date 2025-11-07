#Escribe un programa en Python que realice que extraiga el nombre de usuario y la 
#contraseña de la siguiente cadena: "usuario:root|contraseña:123456"

cadena = "usuario:root|contraseña:123456"

separada = cadena.split("|") #guarda en el array las dos posiciones

usuario = separada[0].split(":") 
nombre = usuario[1]
print("nombre = ", nombre)

contra = separada[1].split(":")
contrasena = contra[1]
print("Contrasena = ", contrasena)