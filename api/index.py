import requests
import flask
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app, resources=r'/*')

@app.route('/hitokoto', methods=["GET"])
def github():
    url = 'https://v1.hitokoto.cn/'
    headers = {
        'accept': '*/*',
        "origin": "http://localhost:4000",
        "referer": "http://localhost:4000/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }
    result = requests.get(url=url, headers=headers, verify=False)
    return result.json()
