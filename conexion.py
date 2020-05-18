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



# # Guardar cambios - commit
# conexion.commit()

# cursor.execute("SELECT * FROM productos")
# productos = cursor.fetchall()
# print(productos)
# print()

# ## Insertar datos
# """
# cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripcion de mi producto', 550)")
# conexion.commit()
# """

# ## Borrar registros
# # cursor.execute("DELETE FROM productos")

# # Insertar muchos registros
# # Una variable con una lista de tuplas las cuales voy a insertar
# productos = [
#     ("Ordenador portatil", "Buen pc", 700),
#     ("Telefono movil", "Buen telefono", 140),
#     ("Placa base", "Buena placa", 80),
#     ("Tablet 15", "Buena tablet", 300),
# ]
# cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos)
# conexion.commit()

# # Actualizar datos
# # SET 'nuevo valor' WHERE 'valor_anterior'
# cursor.execute("UPDATE productos SET precio=678 WHERE precio=80")


# # Listar datos
# # cursor.execute("SELECT * FROM productos") -> Selecciona todos los productos de la base de datos
# cursor.execute("SELECT * FROM productos WHERE precio = 678;")
# # fetchall() -> buscar todos <---> si no hay devuelve lista vacia
# # fetchmany(cantidad) -> buscar hasta la cantidad ingresada <---> si no hay devuelve lista vacia
# # fetchone() -> busca un solo registro (fila) <---> si no hay retorno None
# productos = cursor.fetchall()

# # Imprime todas filas como una lista de tuplas
# print(productos)
# print()

# # Imprimo cada tupla individual de cada producto
# for producto in productos:
#     print(f"ID: {producto[0]}")
#     print(f"Titulo: {producto[1]}")
#     print(f"Descripcion: {producto[2]}")
#     print(f"Precio: {producto[3]}\n")
    

# # Para volver a llamar los 'fetch' debo realizar una consulta nuevamente
# cursor.execute("SELECT titulo from productos;")
# producto = cursor.fetchone()
# print(producto)


