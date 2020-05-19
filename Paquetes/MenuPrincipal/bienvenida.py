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
            print("\n --> Ingreso una opcion incorrecta. Reintente\n")
            opcion = int(input("Ingrese su opcion: "))
        return opcion
    except ValueError:
        print("\n --> Solo se permite el ingreso de números. Reintente.\n")
        return opcionValidacion()
