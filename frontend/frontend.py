# frontend.py
from flask import Flask, render_template_string, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('http://flask-api-service.demo-cni-app.svc.cluster.local/api')
    return render_template_string("""
        <html>
            <body>
                <h1>Load Balancing Demo</h1>
                <p>Response from backend: {{ response.json() }}</p>
                <button onclick="window.location.reload();">Refresh</button>
            </body>
        </html>
    """, response=response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
