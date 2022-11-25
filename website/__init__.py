from flask import Flask, Blueprint, render_template

def create():
    app = Flask(__name__)

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')

    return app
