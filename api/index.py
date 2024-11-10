import requests
import flask
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app, resources=r'/*')

@app.route('/hitokoto', methods=["GET"])
def github(ghpath):
    url = 'https://v1.hitokoto.cn/'
    headers = {
        'accept': 'application/json'
    }
    result = requests.get(url=url, headers=headers, verify=False)
    return result.json()
