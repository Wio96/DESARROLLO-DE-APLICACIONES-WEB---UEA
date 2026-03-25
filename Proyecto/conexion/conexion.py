import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",      # O el host de tu base de datos en la nube
        user="root",           # Tu usuario de MySQL [cite: 2]
        password="123456", 
        database="papangu_tours_final" # El nombre de tu BD [cite: 2]
    )