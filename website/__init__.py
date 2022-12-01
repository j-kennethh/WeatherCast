from flask import Flask, Blueprint
from . import config

def create():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config.API_KEY

    from .view import view
    app.register_blueprint(view, url_prefix='/')

    return app
