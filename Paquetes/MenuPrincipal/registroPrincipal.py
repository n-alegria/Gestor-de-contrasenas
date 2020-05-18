import os, time

def registroPrincipal(conexion, cursor):
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