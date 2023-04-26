from flask import Flask, jsonify
import requests


app = Flask(__name__)


@app.route('/api')
def api():
    response = requests.get('http://app2-service.default.svc.cluster.local/api')
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
