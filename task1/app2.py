from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/api')
def api():
    response = requests.get('https://api.example.com/data')
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
