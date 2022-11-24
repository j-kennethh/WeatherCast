from flask import Flask

def create():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return '<h1>Weatherlens</h1>'

    return app
