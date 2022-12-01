from flask import Flask, Blueprint
from . import config

def create():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config.API_KEY
    app.jinja_env.filters['unix'] = config.unix

    from .view import view
    app.register_blueprint(view, url_prefix='/')

    return app
