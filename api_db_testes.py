#!/usr/local/bin/python3.8
from flask import Flask, request, jsonify
from time import sleep
from database import DATABASE
from formata_json import JsonFy
""" # thread
import threading
 """

app = Flask(__name__)


@ app.route('/ada_api/select/horas/<horas>')
def status(horas):
    status1 = JsonFy().json_data(tempo_coleta=float(horas))
    return {"ADA_stress": status1}


''' @ app.route('/geradores/select/dias/<dias>')
def status_medias(dias):
    status2 = JsonFy().json_minMaxMed_data(float(dias))
    return {"geradores_status": status2}


@ app.route('/geradores/select/horasmedia/<horas>')
def status_medias_horas(horas):
    status3 = JsonFy().json_minMaxMedHora_data(float(horas))
    return {"geradores_status": status3} '''


@app.route('/ada_api/insert', methods=['POST'])
def atualizabanco():
    dados = request.get_json()
    DATABASE().insert_DB(**dados)
    return dados


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9003, debug=False, threaded=True)
