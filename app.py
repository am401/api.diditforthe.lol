import datetime
import random
from flask import json, jsonify
from flask import Flask
from flask import request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description
    })
    response.content_type = "application/json"
    return response

@app.route('/', methods=["GET"])
def hello_world():
    return "Welcome to this marvelous API. Need an integer generated at random? Hit up our only end point: /number\nThanks for visiting..."

@app.route('/number', methods=["GET"])
def random_num():
    rand_int = random.randint(0,99999)
    date_generated = datetime.datetime.now()
    data = {
        "date_generated": date_generated,
        "random_integer": rand_int
    }
    #response = json.dumps(data)
    #mimetype="application/json"
    return jsonify(data)
