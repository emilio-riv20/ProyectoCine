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
                    "id": "4",
                    "nombre": "Super Mario Bros",
                    "fecha": "28/062023",
                    "hora": "17:30",
                    "categoria": "Animación",
                    "link": "https://m.media-amazon.com/images/M/MV5BOTJhNzlmNzctNTU5Yy00N2YwLThhMjQtZDM0YjEzN2Y0ZjNhXkEyXkFqcGdeQXVyMTEwMTQ4MzU5._V1_FMjpg_UX1000_.jpg"
                },
                {
                    "id": "5",
                    "nombre": "Ovnis en Zacapa",
                    "fecha": "30/06/2023",
                    "hora": "13:00",
                    "categoria": "Ciencia Ficción",
                    "link": "https://m.media-amazon.com/images/M/MV5BZGExMmEyMzgtYTQwYy00ZmI0LWI5NjUtNWEwY2M5YjE2ZjU0XkEyXkFqcGdeQXVyNDU0Njk2NTM@._V1_.jpg"
                },
                {
                    "id": "6",
                    "nombre": "Spiderman",
                    "fecha": "30/06/2023",
                    "hora": "15:30",
                    "categoria": "Acción",
                    "link": "https://flxt.tmsimg.com/assets/p13222290_b_v9_ad.jpg"
                },
                {
                    "id": "7",
                    "nombre": "The Batman",
                    "fecha": "01/07/2023",
                    "hora": "10:00",
                    "categoria": "Acción",
                    "link": "https://assets-prd.ignimgs.com/2021/10/15/new-batman-poster-1634314278488.jpg"
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)