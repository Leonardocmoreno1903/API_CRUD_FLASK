from flask_login import UserMixin #Es una clase auxiliar que agrega a la clase User funcionalidades que se requieren para 
# gestionar el inicio de sesión de usuarios, como el manejo de sesiones.
from werkzeug.security import generate_password_hash, check_password_hash
#generate_password_hash y check_password_hash: Son funciones que se utilizan para cifrar las contraseñas de los usuarios y para verificar 
#contraseñas ingresadas contra las almacenadas.

class User(UserMixin):

#Este código define una clase User que hereda de UserMixin y se utiliza principalmente en
#aplicaciones web para gestionar usuarios, contraseñas y privilegios, como en una aplicación de 
#Flask con autenticación.


    def __init__(self, id, name, email, password, is_admin=False):
        #aca definimos el constructor de la clase y le pasamos cinco parametros 
        self.id = id # un identificador de usuario
        self.name = name # un nombre de usuario
        self.email = email # un correo electronico
        self.password = generate_password_hash(password) #un password proporcionado por el usuario que se convierte en un hasd
        self.is_admin = is_admin # esto indica que el usuario no tiene privilegios de administrador
# Este es un método de la clase que permite cambiar la contraseña del usuario. Toma un parámetro 
# password (nueva contraseña) y la cifra usando generate_password_hash(password) para luego almacenarla.
    def set_password(self, password):
        self.password = generate_password_hash(password)

# Este método permite verificar si una contraseña proporcionada por el usuario coincide 
# con la contraseña cifrada almacenada en el objeto.
    def check_password(self, password):
        return check_password_hash(self.password, password)

# Este método Retorna una cadena que muestra el correo electrónico del usuario
    def __repr__(self):
        return '<User {}>'.format(self.email)
    