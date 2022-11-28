from flask import Blueprint, request, redirect, url_for, render_template, flash
import requests
from . import config

view = Blueprint('view', __name__)


@view.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        country = request.form.get('country')

        if not city:
            flash('Must provide a city.', category='error')
            return redirect(url_for('view.index'))
        
        if not country:
            flash('Must provide a country code.', category='error')
            return redirect(url_for('view.index'))

        if len(country) != 2:
            flash('Country code must be 2 letters.', category='error')
            return redirect(url_for('view.index'))

        return redirect(url_for('view.weather', country=country, city=city))
    else: 
        return render_template('index.html')


@view.route('/weather/<country>/<city>', methods=['GET'])
def weather(country, city):
    geo_api = f'http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit=1&appid={config.API_KEY}'
    geo_res = requests.get(geo_api).json()

    if not geo_res:
        flash('Invalid city name or country code, please try again.', category='error')
        return redirect(url_for('view.index'))
    else:
        geo_res = geo_res[0]

    return render_template('weather.html', data=geo_res)
