from flask import Flask,jsonify,request
import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/insert',methods=['POST'])
def insertData():
    cursor = db.mysql.cursor()
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    edad = request.json['edad']
    sexo = request.json['sexo']
    nacionalidad = request.json['nacionalidad']
    profecion = request.json['profecion']
    query = "INSERT INTO datos(nombre,apellido,edad,sexo,nacionaliadad,profecion)values(%s,%s,%s,%s,%s,%s)"
    datos = (nombre,apellido,edad,sexo,nacionalidad,profecion)
    cursor.execute(query,datos)
    db.mysql.commit()
    return jsonify({"respuesta":"operacion exitosa"})   

@app.route('/data',methods=['GET'])
def index():
    #SELECCIONAR DATOS DE LA TABLA EN MYSQL
    cursor = db.mysql.cursor()
    cursor.execute('select * FROM datos')
    resultados = cursor.fetchall()
    respuesta = []
    for resultado in resultados:
        sql = {"id":resultado[0],"nombre":resultado[1],"apellido":resultado[2],"edad":resultado[3],"sexo":resultado[4],"nacionalidad":resultado[5],"profecion":resultado[6]}
        i = respuesta.append(sql)
    return jsonify({"resultados":respuesta})