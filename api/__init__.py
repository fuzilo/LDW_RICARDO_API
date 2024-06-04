from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

app.config["MONGO_URI"] = 'mongodb://localhost:27017/apilol'

mongo = PyMongo(app)
ma = Marshmallow(app)
CORS(app)

from .views import skins_views
