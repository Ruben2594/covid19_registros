import psycopg2
import json

with open ("credenciales.json") as archivo_credenciales:
    credenciales = json.load(archivo_credenciales)
try:
    conexion = psycopg2.connect(**credenciales)
    print("Conexión exitosa a la base de datos. . .")
except psycopg2.Error as e:
    print("Error al conectarse con Base de datos: ", e)