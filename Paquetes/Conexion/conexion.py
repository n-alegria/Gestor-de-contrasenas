#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3, os, time, sys

def conexionBD():
    # Conexión
    try:    
        conexion = sqlite3.connect('./baseDeDatos.db')
        cursor = conexion.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario varchar(255),
            contraseña varchar (255)
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS contraseñas(
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            pagina          varchar(255),
            password        varchar (255),
            id_usuario      integer
        );
        """)
        conexion.commit()
        retorno = (conexion, cursor)
        return retorno
    except:
        os.system("cls")
        print("\nOcurrio un error al intentar conectar con la base de datos.")
        print("Contacte con el administrador")
        time.sleep(2)
        os.system("cls")
