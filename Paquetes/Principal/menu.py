import sys

def menu(opcion):
    if opcion == 1:
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
    elif opcion == 2:
        sys.exit()