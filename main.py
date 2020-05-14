import sys
from Paquetes import bienvenida, menu, opcionValidacion
from Paquetes import conexion


bienvenida()
opcion = opcionValidacion()
menu(opcion)

print("\nGracias por ingresar.")