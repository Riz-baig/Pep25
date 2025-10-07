_num1 = 6
print (type(_num1))
print (type(6))
print ("")

_num2 = _num1
print (type(_num2))
print (type(6))
print ("")

print (_num1 is _num2)
print (_num1 is not _num2)
print  ("")

_num1 = "Hola"
print (type(_num1))
print (type("Hola"))
print (type(6))
print ("")

print(isinstance(_num1, int))
print(isinstance(_num1, str)) 
print(isinstance(_num2, int))
print(isinstance(_num2, str))