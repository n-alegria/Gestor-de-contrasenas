from conexion import conexion

# Almaceno el cursor en la variable 'cursor'
cursor = conexion()

def login(usuario, contraseña):
    if(usuario == 'root' and contraseña == '1a2b3c'):
        return true