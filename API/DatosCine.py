from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route('/getUsuarios', methods=['GET'])
def getUsuario():
    try:
        if request.method == 'GET':
            retorno = [
                {
                    "rol": "cliente",
                    "nombre": "John",
                    "apellido": "Doe",
                    "telefono": "123456789",
                    "correo": "john.doe@example.com",
                    "contrasena": "mipassword123"
                },
                {
                    "rol": "administrador",
                    "nombre": "Jane",
                    "apellido": "Smith",
                    "telefono": "987654321",
                    "correo": "jane.smith@example.com",
                    "contrasena": "password456"
                }
            ]
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)

    except:
        return {"mensaje": "Error interno en el servidor", "status": 500} 
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)