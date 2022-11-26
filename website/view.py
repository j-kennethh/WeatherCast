from flask import Blueprint, request, redirect, url_for, render_template
import requests

view = Blueprint('view', __name__)


@view.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        limit = 1
        API_KEY = 'fa8939ac34315fc99e926f80094f1da3'

        geo_api = f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={API_KEY}'
        geo_res = requests.get(geo_api).json()[0]
        name, country, lat, lon = geo_res['name'], geo_res['country'], geo_res['lat'], geo_res['lon']

        print(f'City: {name}\nCountry: {country}\nLatitude: {lat}\nLongitude: {lon}')
        return redirect(url_for('view.index'))
    else: 
        return render_template('index.html')
