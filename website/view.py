from flask import Blueprint, request, render_template

view = Blueprint('view', __name__)


@view.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    else: 
        return render_template('index.html')
