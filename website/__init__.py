from flask import Flask, Blueprint

def create():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fa8939ac34315fc99e926f80094f1da3'

    from .view import view
    app.register_blueprint(view, url_prefix='/')

    return app
