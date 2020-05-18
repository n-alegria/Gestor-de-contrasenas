import sqlite3

def conexion():
    # Conexión
    conexion = sqlite3.connect('baseDeDatos.db')
    # Crear cursor -> permite ejecutar consultas
    cursor = conexion.cursor()
    # Crear tabla
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario varchar(255),
        contraseña varchar (255)
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contraseñas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pagina varchar(255),
        password varchar (255)
    );
    """)
    ## Guardo cambios
    conexion.commit()
    retorno = (conexion, cursor)
    return retorno
    # Cerrar conexión
    conexion.close()
