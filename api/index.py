import requests
import flask
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app, resources=r'/*')

# 解决文心一言跨域
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

# 解决github跨域
@app.route('/github/<path:ghpath>', methods=["GET", "POST"])
def github(ghpath):
    url = 'https://github.com/{}'.format(ghpath)
    params = {
        'client_id': flask.request.json['client_id'],
        'client_secret': flask.request.json['client_secret'],
        'code': flask.request.json['code']
    }
    headers = {
        'accept': 'application/json'
    }
    result = requests.post(url=url, params=params, headers=headers, verify=False)
    return result.json()
