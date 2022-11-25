from flask import Blueprint, render_template

view = Blueprint('view', __name__)


@view.route('/', methods=['GET'])
def index():
    return render_template('layout.html')
