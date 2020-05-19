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
            print("\n --> Ingreso una opcion incorrecta. Reintente\n")
            opcion = int(input("Ingrese su opcion: "))
        return opcion
    except ValueError:
        print("\n --> Solo se permite el ingreso de números. Reintente.\n")
        return opcionValidacion()
