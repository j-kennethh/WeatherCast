from flask import Blueprint, request, redirect, url_for, render_template, flash
import requests, pprint
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
    
    geo_res = geo_res[0]
    city, country, lat, lon = geo_res['name'], geo_res['country'], round(float(geo_res['lat']), 2), round(float(geo_res['lon']), 2)

    weather_api = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&daily=sunrise,sunset&timezone=auto'
    weather_res = requests.get(weather_api).json()
    pprint.pprint(weather_res)

    photo = {
        0: 'clear.png',

        1: 'mainly-clear.png',
        2: 'partly-cloudy.png',
        3: 'overcast.png',

        45: 'fog.png',
        48: 'fog.png',

        51: 'drizzle.png',
        53: 'drizzle.png',
        55: 'drizzle.png',
        56: 'drizzle.png',
        57: 'drizzle.png',

        61: 'rain.png',
        63: 'rain.png',
        65: 'rain.png',
        66: 'rain.png',
        67: 'rain.png',

        71: 'snow.png',
        73: 'snow.png',
        75: 'snow.png',
        77: 'snow.png',
        85: 'snow.png',
        86: 'snow.png',

        80: 'storm.png',
        81: 'storm.png',
        82: 'storm.png',
        95: 'storm.png',
        96: 'storm.png',
        99: 'storm.png',
    }

    desc = {
        0: 'Clear Skies',

        1: 'Mainly Clear Skies',
        2: 'Partly Cloudy',
        3: 'Overcast',

        45: 'Fog',
        48: 'Depositing Rime Fog',

        51: 'Light Drizzle',
        53: 'Moderate Drizzle',
        55: 'Heavy Drizzle',
        56: 'Light Freezing Drizzle',
        57: 'Heavy Freezing Drizzle',

        61: 'Light Rain',
        63: 'Moderate Rain',
        65: 'Heavy Rain',
        66: 'Light Freezing Rain',
        67: 'Heavy Freezing Rain',

        71: 'Light Snowfall',
        73: 'Moderate Snowfall',
        75: 'Heavy Snowfall',
        77: 'Snow Grains',
        85: 'Light Snow Showers',
        86: 'Heavy Snow Showers',

        80: 'Light Rain Showers',
        81: 'Moderate Rain Showers',
        82: 'Heavy Rain Showers',
        95: 'Thunderstorms',
        96: 'Thunderstorms',
        99: 'Thunderstorms',
    }

    desc = desc[weather_res["current_weather"]["weathercode"]]
    filename = url_for('static', filename=f'{photo[weather_res["current_weather"]["weathercode"]]}')

    return render_template('weather.html', city=city, country=country, data=weather_res, desc=desc, filename=filename)
