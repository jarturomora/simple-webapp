# Importamos la clase Flask del módulo flask para poder crear nuestra aplicación
from flask import Flask, request, jsonify

# Inicializamos una nueva aplicación Flask
app = Flask(__name__)

# Definimos una ruta '/sumar' que aceptará métodos GET
# Esto significa que esta función se ejecutará cuando se acceda a la URL "http://<direccion>/sumar" con el método GET
@app.route('/sumar', methods=['GET'])
def sumar():
    # Obtenemos los parámetros 'a' y 'b' de la URL, por ejemplo, "/sumar?a=10&b=20"
    a = request.args.get('a', type=int)  # Convertimos el valor a entero
    b = request.args.get('b', type=int)  # Convertimos el valor a entero

    # Comprobamos si alguno de los parámetros no existe o es inválido
    if a is None or b is None:
        # Retornamos un mensaje de error con código de estado HTTP 400 (Bad Request)
        return jsonify({'error': 'Faltan los parámetros requeridos o no son enteros'}), 400

    # Realizamos la suma de los números
    result = a + b

    # Retornamos el resultado en formato JSON
    return jsonify({'resultado': result})

# Comprobamos si el archivo es el script principal que se está ejecutando
if __name__ == '__main__':
    # Ejecutamos la aplicación en modo debug para que sea fácil depurar
    app.run(debug=True)
