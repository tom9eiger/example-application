# app.py
from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="Hello, World!", host=socket.gethostname())

@app.route('/api')
def api():
    return jsonify(message="This is the API response", host=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)