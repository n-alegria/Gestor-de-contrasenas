import sys, os
from conexion import conexion

# # Almaceno el cursor en la variable 'cursor'


def main():
    print ("""
    Bienvenido.

        1) Login.
        2) Registro.
        3) Salir.
    """)
    opcion = opcionValidacion()
    if opcion == 1:
        os.system("cls")
        print("Login -->\n")
        cursor = conexion()
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        cursor.execute("SELECT * FROM usuarios WHERE usuario='root' AND contraseña='abc' ")
        login = cursor.fetchone()
        if(login[1] == usuario and login[2] == contraseña):
            print("\n --> Ingreso correcto")
        else:
            print("\n --> Datos ingresados incorrectos.")
    elif opcion == 2:
        os.system("cls")
        print("Registro -->")
    elif opcion == 3:
        os.system("cls")
        print("Gracias por ingresar.")
        sys.exit()

    print("\nGracias por ingresar.")


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

main()