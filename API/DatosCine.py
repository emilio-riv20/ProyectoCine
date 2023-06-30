from flask import Flask, jsonify
from flask import request

import json
app = Flask(__name__)

@app.route('/getUsuarios', methods=['GET'])
def getUsuario():
    try:
        if request.method == 'GET':
            retorno = {
                'usuarios': [
                {
                    "nombre": "Ricardo",
                    "apellido": "Rivera",
                    "telefono": "47512369",
                    "correo": "ricardoriv@gmail.com",
                    "contraseña": "mariokart",
                    "rol": "Cliente"
                },
                {
                    "nombre": "Mario",
                    "apellido": "Humberto",
                    "telefono": "52634789",
                    "correo": "mhriv@gmail.com",
                    "contraseña": "Batman123",
                    "rol": "Cliente"
                }
                ]
            }
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)

    except:
        return {"mensaje": "Error interno en el servidor", "status": 500} 
    
@app.route('/getPeliculas', methods=['GET'])
def getPeliculas():
    try:
        if request.method == 'GET':
            retorno = {
                'pelicula': [
                {
                    "id": "6",
                    "nombre": "Super Mario Bros",
                    "fecha": "2023-06-28",
                    "hora": "17:30",
                    "categoria": "Animación",
                    "link": "https://acortar.link/JbuxgS"
                },
                {
                    "id": "7",
                    "nombre": "Ovnis en Zacapa",
                    "fecha": "2023-06-30",
                    "hora": "13:00",
                    "categoria": "Ciencia Ficción",
                    "link": "https://acortar.link/pNEnSj"
                },
                {
                    "id": "8",
                    "nombre": "Spiderman",
                    "fecha": "2023-06-30",
                    "hora": "15:30",
                    "categoria": "Acción",
                    "link": "https://acortar.link/dKEwnJ"
                },
                {
                    "id": "9",
                    "nombre": "The Batman",
                    "fecha": "2023-07-01",
                    "hora": "10:00",
                    "categoria": "Acción",
                    "link": "https://acortar.link/qKNE9K"
                }
                ]
            }
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)

    except:
        return {"mensaje": "Error interno en el servidor", "status": 500} 
    
@app.route('/getSalas', methods=['GET'])
def getSalas():
    try:
        if request.method == 'GET':
            retorno = {
                'sala': [
                {
                    "numero": "4",
                    "asientos": "200",
                },
                {
                    "numero": "5",
                    "asientos": "190",
                },
                {
                    "numero": "6",
                    "asientos": "150"
                }
                ]
            }
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)

    except:
        return {"mensaje": "Error interno en el servidor", "status": 500} 
    
@app.route('/getTarjeta', methods=['GET'])
def getTarjeta():
    try:
        if request.method == 'GET':
            retorno = {
                'tarjeta': [
                {
                    "tipo": "Debito",
                    "numero": "7895615165463164",
                    "titular": "Ricardo Rivera",
                    "fecha": "2023-06-30"
                },
                {
                    "tipo": "Credito",
                    "numero": "748851321681321",
                    "titular": "Mario Humberto",
                    "fecha": "2023-06-30"
                }
                ]
            }
        else:
            retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)

    except:
        return {"mensaje": "Error interno en el servidor", "status": 500} 
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)