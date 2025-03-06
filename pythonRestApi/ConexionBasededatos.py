import mysql.connector # con esta linea importamos los controladores necesarios para realizar la conexion con la BD
from mysql.connector import Error

class ConexionMysql: #creamos esta clase y a traves de ella se importara la conexion a cada tabla que contenga la BD
    def __init__(self): # cada clase debe tener un constructor
        try:
            self.mibasededatos = mysql.connector.connect( #en esta variable estoy guardando los controladores para realizar la conexion con la BD
                host="localhost",
                port="3306", #este es el puerto que aparece en Xampp de MySQL
                user="root",
                password="",
                database="prueba" # Este es el nombre de la base de datos que vamos a utilizar 
        )
            self.conexion = self.mibasededatos
            self.cursor = self.conexion.cursor()    

        # Se verifica si la conexión está activa antes de obtener información sobre el servidor
        
            if self.mibasededatos.is_connected():
                db_Info = self.mibasededatos.get_server_info()
                print(f"Connected to MySQL Server, version:, {db_Info}")

        except Error as e:
            print(f"Error al conectar con MySQL: {e}")

    def cerrar_conexion(self):
        # Cierra el cursor y la conexión al finalizar
        if self.mibasededatos.is_connected():
            self.cursor.close()
            self.conexion.close()
            print("Conexion cerrada correctamente")

if __name__ == "__main__":
    conexion = ConexionMysql()
    conexion.cerrar_conexion()
