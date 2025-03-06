import mysql.connector

class ConexionMysql:
    def __init__(self):
        self.mibasededatos = mysql.connector.connect(
            host="localhost",
            port="3306",
            user="root",
            password="",
            database="prueba"
        )
        self.conexion = self.mibasededatos
        self.cursor = self.conexion.cursor()

        # Se verifica si la conexión está activa antes de obtener información sobre el servidor
        if self.mibasededatos.is_connected():
            db_Info = self.mibasededatos.get_server_info()
            print("Connected to MySQL Server version:", db_Info)

    def cerrar_conexion(self):
        # Cierra el cursor y la conexión al finalizar
        self.cursor.close()
        self.conexion.close()
