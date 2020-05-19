#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, time
from Paquetes import bienvenida, loginPrincipal, registroPrincipal


def main():
    os.system("cls")
    opcion = bienvenida()
    if opcion == 1:
        loginPrincipal()
        main()
    elif opcion == 2:
        registroPrincipal()
        main()
    
    print("\nGracias por ingresar.")
    time.sleep(2)
    os.system("cls")
    sys.exit()

    


main()