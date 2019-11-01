import os
from flask import Flask, session
from flask_session import Session
from flask.ext.pymongo import PyMongo

mongo = PyMongo()

def create_app():
    config_name = os.environ.get('FLASK_CONFIG', 'development')

    app = Flask(__name__)
    app.config.from_object('config_' + config_name)
    Session(app)
    #mongo.init_app(app)

    from .hotel import hotel as hotel_blueprint
    app.register_blueprint(hotel_blueprint)

    return app
