
from ModelProductos import ModelProductos
from ModelUsuario import ModelUsuarios
#con la siguientes lineas importamos el modulo del login
from flask_login import LoginManager


from flask import Flask , jsonify , request
from flask_cors import CORS


app = Flask(__name__)
#dado que flask-login hace uso de la sesion de autenticación debemos establecer la variable de configuracion secret key
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'


#login_manager = LoginManager(app)
CORS(app)  # Configura CORS en tu aplicación Flask (es esencial cuando se trabaja con aplicaciones frontend y backend separadas)
# codigo para ejecutar el servidor de (flask --app Controladores run) esto se usa para postman


productos = ModelProductos()
usuarios = ModelUsuarios()


@app.route('/login', methods=['POST'])
def loginUsuario():
    email = request.json['email']
    password = request.json['password']
    resultado = usuarios.verificarUsuario(email, password)
    return jsonify({"mensaje": resultado})
     


@app.route('/productos', methods=['GET'])
def listarproductos():
     return jsonify(productos.obtener_productos())


@app.route('/producto/<int:id>', methods=['GET'])
def producto(id):
     return  jsonify(productos.obtener_producto(id))
     
@app.route('/nuevo_producto', methods=['POST'])
def crear_producto():
     nombre = request.json['nombre']
     precio = request.json['precio']
     productos.insertar_producto(nombre,precio)
     return jsonify({"mensaje": "producto creado exitosamente"})


@app.route('/actualizar_producto/<int:id>', methods=['PUT'])
def actualizar_producto(id):
     data = request.json
     nombre = data.get('nombre')
     precio = data.get('precio')

     if nombre is None and precio is None:
          return jsonify({"error": "No se proporcionaron datos para actualizar"}), 400
     else:
          productos.actualizar_producto(id,nombre,precio)
          return jsonify({"mensaje": "Producto actualizado correctamente"})


@app.route('/eliminar_producto/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
     if productos.obtener_producto(id):
          productos.eliminar_producto(id)
          return jsonify({"mensaje": "Producto eliminado correctamente"})
     else:
          return jsonify({"error": "El producto no existe"}), 404



@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
     return jsonify(usuarios.obtener_usuarios())

@app.route('/nuevo_usuario', methods=['POST'])
def crear_usuario():
     nombre = request.json['nombre']
     email = request.json['email']
     contrasena = request.json['contrasena']
     usuarios.insertar_usuario(nombre, email, contrasena)
     return jsonify({"mensaje": "Usuario creado exitosamente"})

@app.route('/actualizar_usuario/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
     data = request.json
     nombre = data.get('nombre')
     email = data.get('email')
     contrasena = data.get('contrasena')

     if nombre is None and email is None and contrasena is None:
          return jsonify({"error": "No se proporcionaron datos para actualizar"}), 400

     usuario_existente = usuarios.obtener_usuario(id)
     if usuario_existente:

          usuarios.actualizar_usuario(id, nombre, email, contrasena)
          return jsonify({"mensaje": "Usuario actualizado correctamente"})
     else:
          return jsonify({"error": "El usuario no existe"}), 404

@app.route('/eliminar_usuario/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
     if usuarios.obtener_usuario(id):
          usuarios.eliminar_usuario(id)
          return jsonify({"mensaje": "Usuario eliminado correctamente"})
     else:
          return jsonify({"error": "El usuario no existe"}), 404


if __name__ == '__main__':
     app.run(debug=True)
     


     



     




