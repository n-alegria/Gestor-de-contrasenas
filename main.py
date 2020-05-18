#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, time
from conexion import conexion


def main():
    print ("""
    Bienvenido.

        1) Login.
        2) Registro.
        3) Salir.
    """)
    opcion = opcionValidacion()
    if opcion == 1:
        limpiarPantalla()
        print("Login -->\n")
        # # Almaceno el cursor en la variable 'cursor'
        retorno = conexion()
        con = retorno[0]
        cursor = retorno[1]
        usuario = input("Ingrese su usuario: ")
        contraseña = input("Ingrese su contraseña: ")
        cursor.execute(f"SELECT * FROM usuarios WHERE usuario='{usuario}' AND contraseña='{contraseña}' ")
        verificado = cursor.fetchone()
        if(verificado[1] == usuario and verificado[2] == contraseña):
            print("\n --> Ingreso correcto")
            time.sleep(1)
            login(con, cursor, verificado)
        else:
            print("\n --> Datos ingresados incorrectos.")
    elif opcion == 2:
        limpiarPantalla()
        print("Registro -->")
    elif opcion == 3:
        limpiarPantalla()
        print("Gracias por ingresar.")
        sys.exit()

    print("\nGracias por ingresar.")



### Funciones -->

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

def limpiarPantalla():
    os.system("cls")

def login(con, cursor, verificado):
    limpiarPantalla()
    print(f"""
    Bienvenido {verificado[1]}.

        1) Alta de contraseña.
        2) Baja de contraseña.
        3) Modificar contraseña.
        4) Mostrar todas las contraseñas.
        5) Volver al menú.
    """)
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        limpiarPantalla()
        print(" --> Alta de contraseña <--\n")
        pagina = input("Ingrese el nombre de la pagina: ")
        contraseña = input("Ingrese la contraseña de la pagina: ")
        reContraseña = input("Reingrese la contraseña: ")
        if contraseña == reContraseña:
            ## Primera forma
            cursor.execute(f"INSERT INTO contraseñas VALUES (null, ?, ?)", (pagina, contraseña))
            con.commit()
            if cursor.rowcount > 0:
                print("Ingreso exitoso.")
            login(con, cursor, verificado)
        else:
            print("\nError, las contraseñas no coinciden.")
    elif opcion == 2:
        limpiarPantalla()
        print(" --> Baja de contraseña <--\n")
        pagina = input("Ingrese la pagina a borrar: ")
        cursor.execute(f"SELECT * FROM contraseñas WHERE pagina = '{pagina}'")
        existe = cursor.fetchone()
        if existe != None:
            confirma = input("\nConfirma que desea eliminar la pagina (s/n): ")
            if confirma == 's':
                cursor.execute(f"DELETE FROM contraseñas WHERE pagina = '{pagina}'")
                con.commit()
                if cursor.rowcount > 0:
                    print("\nSe elimino la pagina exitosamente.")
                    os.system("pause")
            else:
                print("\nSe cancelo la baja de la pagina")
        else:
            print(f"\nNo existe la pagina '{pagina}'")
        login(con, cursor, verificado)
    elif opcion == 3:
        limpiarPantalla()
        print(" --> Modificar contraseña <--\n")
        pagina = input("Ingrese la pagina: ")
        cursor.execute(f"SELECT * FROM contraseñas WHERE pagina = '{pagina}'")
        existe = cursor.fetchone()
        if existe != None:
            print(f"""
        +--------------------------------------+
        |   Pagina              Contraseña     |
        |--------------------------------------|
        |  {existe[1]:14}      {existe[2]:14}  |
        +--------------------------------------+\
        """)
            nuevaContraseña = input("\nIngrese la nueva contraseña: ")
            reNuevaContraseña = input("Ingrese nuevamente la contraseña: ")
            if nuevaContraseña == reNuevaContraseña:
                confirma = input("\nConfirma que desea modificar la pagina (s/n): ")
                if confirma == 's':
                    cursor.execute(f"UPDATE contraseñas SET password = '{nuevaContraseña}' WHERE pagina = '{pagina}'")
                    con.commit()
                    if cursor.rowcount > 0:
                        print("\nSe modifico la contraseña exitosamente.")
                        os.system("pause")
                else:
                    print("\nSe cancelo la modificacion de contraseña")
        else:
            print(f"\nNo existe la pagina '{pagina}'")
        login(con, cursor, verificado)
    elif opcion == 4:
        limpiarPantalla()
        print(" --> Listado de contraseñas <--\n")
        cursor.execute("SELECT * FROM contraseñas")
        listaContraseñas = cursor.fetchall()
        Tabla = """\
+--------------------------------------+
|   Pagina              Contraseña     |
|--------------------------------------|
{}
+--------------------------------------+\
"""
        Tabla = (Tabla.format("\n".join(f"|  {contraseña[1]:14}       {contraseña[2]:14} |".format(contraseña)
        for contraseña in listaContraseñas)))
        print(Tabla)
        print()
        os.system("pause")
        login(con, cursor, verificado)
    elif opcion == 5:
        print(f"\nHasta luego {verificado[1]}")
        del verificado
        con.close()
        time.sleep(1)
        limpiarPantalla()
        main()

main()