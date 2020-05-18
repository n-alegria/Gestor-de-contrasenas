import os

def bienvenida(usuario):
    os.system("cls")
    print(f"""
    Bienvenido {usuario[1]}.

        1) Alta de contraseña.
        2) Baja de contraseña.
        3) Modificar contraseña.
        4) Mostrar todas las contraseñas.
        5) Volver al menú.
    """)
    opcion = opcionValidacion()
    return opcion

def opcionValidacion():
    try:
        opcion = int(input("Ingrese su opcion: "))
        while (opcion <= 0 or opcion >= 6):
            print("\nIngreso una opcion incorrecta. Reintente")
            opcion = int(input("Ingrese su opcion: "))
        return opcion
    except:
        print("\n<-- Su ingreso no es valido, reintente. -->\n")
        opcionValidacion()