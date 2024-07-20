import tkinter
from tkinter import *
from tkinter import messagebox,filedialog
import pymysql
import shutil
import os


try:
    # Conectar a la base de datos
    conn = pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="bd2"
    )

    with conn.cursor() as cursor:
        # Ejecutar una consulta
        query = "SELECT id, pelicula, imagen FROM prueba"
        cursor.execute(query)

        # Obtener los nombres de las columnas
        column_names = [desc[0] for desc in cursor.description]

        # Obtener los resultados
        results = cursor.fetchall()

        # Procesar los resultados
        for row in results:
            data = dict(zip(column_names, row))

            id = data['id']
            pelicula = data['pelicula']
            imagen = data['imagen']

            # Hacer algo con los valores
            print(f"ID: {id}, Pelicula: {pelicula}, Ruta imagen: {imagen}")

except pymysql.MySQLError as e:
    print(f"Error: {e}")




