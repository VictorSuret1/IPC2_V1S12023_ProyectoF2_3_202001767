from flask import Flask, jsonify
from flask import request

app =Flask(__name__)
@app.route('/getUsuarios',methods=['GET'])
def getUser():
    try:
        if request.method == 'GET':
            retorno ={
                "usuario": [
                                {
                                    "rol": "cliente",
                                    "nombre": "Jorge",
                                    "apellido": "Diaz",
                                    "telefono": "11111",
                                    "correo": "jorgeD@example.com",
                                    "contrasena": "pass"
                                },
                                {
                                    "rol": "cliente",
                                    "nombre": "Joana",
                                    "apellido": "Paz",
                                    "telefono": "12312312",
                                    "correo": "JoaP@example.com",
                                    "contrasena": "pass2"
                                },
                                {
                                    "rol": "cliente",
                                    "nombre": "Pablito",
                                    "apellido": "Pablon",
                                    "telefono": "2222",
                                    "correo": "Pablito@example.com",
                                    "contrasena": "pass3"
                                }
                            ]
                    }
        else:
             retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}
    

@app.route('/getSalas',methods=['GET'])
def getSalas():
    try:
        if request.method == 'GET':
            retorno ={
                    "cine": {
                        "nombre": "Cine ABC2",
                        "salas": {
                            "sala": [
                                {
                                    "numero": "#USACIPC2_202212333_4",
                                    "asientos": "500"
                                },
                                {
                                    "numero": "#USACIPC2_202212333_5",
                                    "asientos": "400"
                                },
                                {
                                    "numero": "#USACIPC2_202212333_6",
                                    "asientos": "700"
                                }
                            ]
                        }
                    }
            }
        else:
             retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}
    


@app.route('/getPeliculas',methods=['GET'])
def getPeliculas():
    try:
        if request.method == 'GET':
            retorno ={
                "categoria": [
                {
                    "nombre": "Aventura",
                    "peliculas": {
                        "pelicula": [
                            {
                                "titulo": "Las momias del faraon",
                                "director": "Luc Besson",
                                "anio": "2010",
                                "fecha": "2023-02-05",
                                "hora": "19:30",
                                "imagen": "https://es.web.img2.acsta.net/medias/nmedia/18/78/77/56/19477844.jpg",
                                "precio": "52"
                            },
                            {
                                "titulo": "Aladdin",
                                "director": "Chad Stahelski",
                                "anio": "2019",
                                "fecha": "2023-06-06",
                                "hora": "20:00",
                                "imagen": "https://m.media-amazon.com/images/M/MV5BMjQ2ODIyMjY4MF5BMl5BanBnXkFtZTgwNzY4ODI2NzM@._V1_FMjpg_UX1000_.jpg",
                                "precio": "55"
                            },
                            {
                                "titulo": "Jurassic Park",
                                "director": "Steven Spielberg",
                                "anio": "1993",
                                "fecha": "2023-07-15",
                                "hora": "18:30",
                                "imagen": "https://m.media-amazon.com/images/M/MV5BMjM2MDgxMDg0Nl5BMl5BanBnXkFtZTgwNTM2OTM5NDE@._V1_FMjpg_UX1000_.jpg",
                                "precio": "60"
                            }
                        ]
                    }
                }
            ]}
        else:
             retorno = {'mensaje': 'Error en la petición, método incorrecto'}
        return jsonify(retorno)
    except:
        return {"mensaje": "Error interno en el servidor", "status": 500}
    
@app.route('/getTarjetas',methods=['GET'])
def getTarjetas():
    try:
        if request.method == 'GET':
            retorno ={
                "tarjeta": [
                            {
                            "tipo": "Debito",
                            "numero": "0123456789",
                            "titular": "Patito Juan",
                            "fecha_expiracion": "12/2028"
                            },
                            {
                            "tipo": "Credito",
                            "numero": "9876543210",
                            "titular": "Tony Stark",
                            "fecha_expiracion": "01/2025"
                            },
                            {
                            "tipo": "Debito",
                            "numero": "1245789630",
                            "titular": "Bruce Lee",
                            "fecha_expiracion": "10/2024"
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