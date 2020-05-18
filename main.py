#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, time
from Paquetes import conexionBD, bienvenida, loginPrincipal, registroPrincipal


def main():
    retorno = conexionBD()
    conexion = retorno[0]
    cursor = retorno[1]
    opcion = bienvenida()
    if opcion == 1:
        loginPrincipal(conexion, cursor)
        main()
    elif opcion == 2:
        registroPrincipal(conexion, cursor)
        main()
    elif opcion == 3:
        print("\nGracias por ingresar.")
        sys.exit()

    print("\nGracias por ingresar.")


main()