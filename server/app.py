from flask import Flask,jsonify
from db import respuesta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/datos')
def index():
    return jsonify({"resultados":respuesta})