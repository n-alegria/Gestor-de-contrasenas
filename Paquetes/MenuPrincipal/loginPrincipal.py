import os, time, sys, getpass
from ..MenuContraseñas import menuContraseñas
from ..Conexion import conexionBD
from sqlite3.dbapi2 import OperationalError

def loginPrincipal():
    retorno = conexionBD()
    conexion = retorno[0]
    cursor = retorno[1]
    os.system("cls")
    print("  Login -->\n")
    usuario = input("Ingrese su usuario: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    cursor.execute(f"SELECT * FROM usuarios WHERE usuario='{usuario}' AND contraseña='{contraseña}' ")
    verificado = cursor.fetchone()
    if verificado != None:
        print("\n --> Ingreso correcto")
        time.sleep(1)
        menuContraseñas(conexion, cursor, verificado)
    else:
        print("\nUsuario y/o contraseñas incorrectos.\nReintente.\n")
        os.system("pause")

    os.system("cls")