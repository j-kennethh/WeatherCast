from flask import Flask, Blueprint

def create():
    app = Flask(__name__)

    from .view import view
    app.register_blueprint(view, url_prefix='/')

    return app
