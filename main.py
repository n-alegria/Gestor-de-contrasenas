#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, time
from Paquetes import conexionBD, bienvenida, loginPrincipal


def main():
    retorno = conexionBD()
    conexion = retorno[0]
    cursor = retorno[1]
    opcion = bienvenida()
    if opcion == 1:
        loginPrincipal(conexion, cursor)
    elif opcion == 2:
        os.system("cls")
        print("Registro -->\n")
        nombreUsuario = input("Nombre de usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        reContraseña = input("Reingrese su contraseña: ")
        if contraseña == reContraseña:
            cursor.execute(f"INSERT INTO usuarios VALUES (null, ?, ?)", (nombreUsuario, contraseña))
            conexion.commit()
            if cursor.rowcount > 0:
                print("\nIngreso exitoso.")
                time.sleep(1)
                os.system("cls")
        else:
            print("\nError, las contraseñas no coinciden.")
        main()
    elif opcion == 3:
        print("\nGracias por ingresar.")
        sys.exit()

    print("\nGracias por ingresar.")


main()