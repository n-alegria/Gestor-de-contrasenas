import os, time
from ..MenuContraseñas import menuContraseñas

def loginPrincipal(conexion, cursor):
    os.system("cls")
    print("  Login -->\n")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    cursor.execute(f"SELECT * FROM usuarios WHERE usuario='{usuario}' AND contraseña='{contraseña}' ")
    verificado = cursor.fetchone()
    if(verificado[1] == usuario and verificado[2] == contraseña):
        print("\n --> Ingreso correcto")
        time.sleep(1)
        menuContraseñas(conexion, cursor, verificado)
    else:
        print("\n --> Datos ingresados incorrectos.")