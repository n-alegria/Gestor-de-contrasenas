import os, time
from Paquetes.MenuContraseñas.bienvenida import bienvenida


def loginContraseñas(conexion, cursor, verificado):
    opcion = bienvenida(verificado)
    if opcion == 1:
        os.system("cls")
        print(" --> Alta de contraseña <--\n")
        pagina = input("Ingrese el nombre de la pagina: ")
        contraseña = input("Ingrese la contraseña de la pagina: ")
        reContraseña = input("Reingrese la contraseña: ")
        if contraseña == reContraseña:
            cursor.execute(f"INSERT INTO contraseñas VALUES (null, ?, ?, ?)", (pagina, contraseña, verificado[0]))
            conexion.commit()
            if cursor.rowcount > 0:
                print("\nIngreso exitoso.\n")
                os.system("pause")
            loginContraseñas(conexion, cursor, verificado)
        else:
            print("\nError, las contraseñas no coinciden.")
    elif opcion == 2:
        os.system("cls")
        print(" --> Baja de contraseña <--\n")
        pagina = input("Ingrese la pagina a borrar: ")
        cursor.execute(f"SELECT * FROM contraseñas WHERE pagina = '{pagina}' AND id_usuario = '{verificado[0]}'")
        existe = cursor.fetchone()
        if existe != None:
            confirma = input("\nConfirma que desea eliminar la pagina (s/n): ")
            if confirma == 's':
                cursor.execute(f"DELETE FROM contraseñas WHERE pagina = '{pagina}'")
                conexion.commit()
                if cursor.rowcount > 0:
                    print("\nSe elimino la pagina exitosamente.")
                    os.system("pause")
            else:
                print("\nSe cancelo la baja de la pagina")
        else:
            print(f"\nNo existe la pagina '{pagina}'")
        loginContraseñas(conexion, cursor, verificado)
    elif opcion == 3:
        os.system("cls")
        print(" --> Modificar contraseña <--\n")
        pagina = input("Ingrese la pagina: ")
        cursor.execute(f"SELECT * FROM contraseñas WHERE pagina = '{pagina}' AND id_usuario = '{verificado[0]}'")
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
                    conexion.commit()
                    if cursor.rowcount > 0:
                        print("\nSe modifico la contraseña exitosamente.")
                        os.system("pause")
                else:
                    print("\nSe cancelo la modificacion de contraseña")
        else:
            print(f"\nNo existe la pagina '{pagina}'")
        loginContraseñas(conexion, cursor, verificado)
    elif opcion == 4:
        os.system("cls")
        print(" --> Listado de contraseñas <--\n")
        cursor.execute(f"SELECT * FROM contraseñas WHERE id_usuario = '{verificado[0]}' ")
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
        loginContraseñas(conexion, cursor, verificado)
    elif opcion == 5:
        print(f"\nHasta luego {verificado[1]}")
        del verificado
        conexion.close()
        time.sleep(1)
        os.system("cls")