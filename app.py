# app_b.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hola Gustavo Contreras desde app B', 200

@app.route('/startup', methods=['GET'])
def startup_probe():
    return jsonify(status='starting'), 200

@app.route('/readiness', methods=['GET'])
def readiness_probe():
    return jsonify(status='ready'), 200

@app.route('/health', methods=['GET'])
def liveness_probe():
    return jsonify(status='healthy'), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
