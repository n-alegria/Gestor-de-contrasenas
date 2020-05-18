def bienvenida():
    print ("""
    Bienvenido.

        1) Login.
        2) Registro.
        3) Salir.
    """)
    opcion = opcionValidacion()
    return opcion

def opcionValidacion():
    try:
        opcion = int(input("Ingrese su opcion: "))
        while (opcion != 1 and opcion != 2 and opcion != 3):
            print("\nIngreso una opcion incorrecta. Reintente")
            opcion = int(input("Ingrese su opcion: "))
        return opcion
    except:
        print("\n<-- Su ingreso no es valido, reintente. -->\n")
        opcionValidacion()