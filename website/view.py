from flask import Blueprint, request, redirect, url_for, render_template
import requests

view = Blueprint('view', __name__)


@view.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        return redirect(f'/weather/{city}')
    else: 
        return render_template('index.html')


@view.route('/weather/<city>', methods=['GET'])
def weather(city):
    API_KEY = 'fa8939ac34315fc99e926f80094f1da3'
    geo_api = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}'
    geo_res = requests.get(geo_api).json()[0]

    return render_template('weather.html', data=geo_res)
