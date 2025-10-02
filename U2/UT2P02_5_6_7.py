#Escribe un programa que pida dos números y que indique cuál es el menor, cuál el mayor 
#o que indique que son iguales.
num1 = int(input("indicame el primer numero: "))
num2 = int(input("indicame el segundo numero: "))
if num1 > num2:
    print("el primer numero es mayor que el segundo.")
elif num2 > num1:
    print("el segundo numero es mayor que el primero.")
else:
    print("Los dos numeros son iguales.")

#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta
dia = int(input("indica dia"))
mes = int(input("indica el mes"))
anno = int(input("indica el año"))

if dia > 31 or dia < 1:
    print("el dia debe estar comprendido entre 1 y 31")
elif mes > 12 or mes < 1:
    print("el mes debe esta comprendido entre 1 y 12")
elif anno < 1 or anno > 9999:
    print("el año no puede ser de 5 digitos")
else:
    print("La fecha es ", dia,"/", mes, "/",anno)

#Escriba un programa que pida un año y que escriba si es bisiesto o no. Un año es bisiesto 
#si es múltiplos de 4 pero no múltiplos de 100, aunque si los múltiplos de 400.
anno = int(input("Indica el año: "))

if anno < 1 or anno > 9999:
    print("El año debe estar comprendido entre 1 y 9999")
elif (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
    print("El año",anno, "es bisiesto")
else:
    print("El año ",anno, "no es bisiesto")

