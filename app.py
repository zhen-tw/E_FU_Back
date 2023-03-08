# app.py
from flask import Flask
from itsdangerous import TimedJSONWebSignatureSerializer as TJSS

from controller import(user,record,people)
from model.db import mongo
from controller.util import checkParm, ret


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ABCDEFhijklm'
app.config["MONGO_URI"] = "mongodb+srv://numbone112:i3PO8xrZj1KRwz83@cluster0.5rqnhen.mongodb.net/efu"
mongo.init_app(app) # initialize here!
print(type(mongo))
print((mongo.db.name))
app.register_blueprint(user.userProfile)
app.register_blueprint(people.peopleProfile)

app.register_blueprint(record.recordAPI)


@app.route('/', methods=["POST"])
def line():
    return "ok"


@app.route('/get', methods=["GET","OPTIONS"])
def home():
    return 'good from backend'
