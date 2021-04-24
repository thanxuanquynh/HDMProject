from flask import Flask, jsonify, request
import json
from database.connection import *
from database.env import *
from datetime import date, datetime, timedelta

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'not found '+ request.url
    }
    res = jsonify(message)
    res.status_code = 404
    return res


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/register', methods=['POST'])
def register_user():
    data = json.loads(request.data.decode("utf-8"))
    user_data = {
        'username' : data['username'],
        'password' : data['password'],
        'created_at' : datetime.now(),
        'updated_at' : datetime.now()
    }
    res = insert_database(Enum_Table.user.value, user_data)
    message = {
        'register': res
    }
    resp = jsonify(message)
    resp.status_code = 200
    return resp


@app.route('/login', methods=['POST'])
def login_user():
    data = json.loads(request.data.decode("utf-8"))
    user_data = {
        'username': data['username'],
        'password': data['password']
    }
