import os, time
from ..MenuContraseñas.bienvenida import bienvenida

def menuContraseñas(conexion, cursor, usuarioVerificado):
    opcion = bienvenida(usuarioVerificado)
    if opcion == 1:
        altaContraseña(conexion, cursor, usuarioVerificado)
    elif opcion == 2:
        bajaContraseña(conexion, cursor, usuarioVerificado)
    elif opcion == 3:
        modificarContraseña(conexion, cursor, usuarioVerificado)
    elif opcion == 4:
        listarContraseñas(conexion, cursor, usuarioVerificado)
    elif opcion == 5:
        volverPrincipal(conexion, usuarioVerificado)


## Funciones -->

def altaContraseña(conexion, cursor, usuarioVerificado):
    os.system("cls")
    print(" --> Alta de contraseña <--\n")
    pagina = input("Ingrese el nombre de la pagina: ")
    contraseña = input("Ingrese la contraseña de la pagina: ")
    reContraseña = input("Reingrese la contraseña: ")
    if contraseña == reContraseña:
        cursor.execute(f"INSERT INTO contraseñas VALUES (null, ?, ?, ?)", (pagina, contraseña, usuarioVerificado[0]))
        conexion.commit()
        if cursor.rowcount > 0:
            print("\n --> Ingreso exitoso.\n")
    else:
        print("\n --> Error, las contraseñas no coinciden.\n")    
    os.system("pause")
    menuContraseñas(conexion, cursor, usuarioVerificado)


def bajaContraseña(conexion, cursor, usuarioVerificado):
    os.system("cls")
    print(" --> Baja de contraseña <--\n")
    pagina = input("Ingrese la pagina a borrar: ")
    cursor.execute(f"SELECT * FROM contraseñas WHERE pagina = '{pagina}' AND id_usuario = '{usuarioVerificado[0]}'")
    existe = cursor.fetchone()
    if existe != None:
        confirma = input("\n¿Confirma que desea eliminar la pagina? (s/n): ").lower()
        if confirma == 's':
            cursor.execute(f"DELETE FROM contraseñas WHERE pagina = '{pagina}'")
            conexion.commit()
            if cursor.rowcount > 0:
                print("\n --> Se elimino la pagina exitosamente.\n")
            else:
                print("\n --> No fue posible eliminar la pagina.")
        else:
            print("\n --> Se cancelo la baja de la pagina.\n")
    else:
        print(f"\n --> No existe la pagina '{pagina}'\n")
    os.system("pause")
    menuContraseñas(conexion, cursor, usuarioVerificado)


def modificarContraseña(conexion, cursor, usuarioVerificado):
    os.system("cls")
    print(" --> Modificar contraseña <--\n")
    pagina = input("Ingrese la pagina: ")
    cursor.execute(f"SELECT * FROM contraseñas WHERE pagina = '{pagina}' AND id_usuario = '{usuarioVerificado[0]}'")
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
            confirma = input("\nConfirma que desea modificar la pagina (s/n): ").lower()
            if confirma == 's':
                cursor.execute(f"UPDATE contraseñas SET password = '{nuevaContraseña}' WHERE pagina = '{pagina}' AND id_usuario = '{usuarioVerificado[0]}'")
                conexion.commit()
                if cursor.rowcount > 0:
                    print("\n --> Se modifico la contraseña exitosamente.\n")
                else:
                    print("\n --> No fue posible modificar la contraseña\n.")
            else:
                print("\n --> Se cancelo la modificacion de contraseña.\n")
        else:
            print("\n --> Error, las contraseñas no coinciden.\n")
    else:
        print(f"\n --> No existe la pagina '{pagina}'\n")
    os.system("pause")
    menuContraseñas(conexion, cursor, usuarioVerificado)


def listarContraseñas(conexion, cursor, usuarioVerificado):
    os.system("cls")
    print(" --> Listado de contraseñas <--\n")
    cursor.execute(f"SELECT * FROM contraseñas WHERE id_usuario = '{usuarioVerificado[0]}' ")
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
    print(f"{Tabla}\n")
    os.system("pause")
    menuContraseñas(conexion, cursor, usuarioVerificado)


def volverPrincipal(conexion, usuarioVerificado):
    print(f"\n--> Hasta luego {usuarioVerificado[1]}")
    del usuarioVerificado
    conexion.close()
    time.sleep(1)