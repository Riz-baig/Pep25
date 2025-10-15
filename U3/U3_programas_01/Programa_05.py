variable_global = "la variable de ámbito global, invocada en función interna"

def funcion_externa():
    variable_no_local = "variable no local, es para usar en una función"

    def funcion_interna():
        nonlocal variable_no_local   # permite modificar la variable de la función externa
        variable_local = "variable que solo se usa en esta función"
        variable_no_local = "La variable de otra función, modificada aqui."

        print(variable_local)       # se puede usar solo dentro de esta función
        print(variable_no_local)    # accede a la variable de la función externa
        print(variable_global)      # accede a la variable global

    funcion_interna()
    print(variable_no_local)        # ya modificada por la función interna
    print(variable_global)          # accede a la global desde la función externa


funcion_externa()# llamo a la función externa, que tiene una función interna, que recibe variable global, no local etc


