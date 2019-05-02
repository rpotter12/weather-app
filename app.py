from flask import Flask, render_template, jsonify, request, redirect, url_for
import requests

app = Flask(__name__, static_url_path='/static')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/weather_info', methods=['POST'])
def weather_info():
    city_input = request.form["weather"]
    # Setup OpenWeatherMap API
    api_key = 'xxxxxx_openweather_key_xxxxxx'    
    celsius = 'metric'
    url = f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city_input}&units={celsius}'
    response = requests.get(url).json()    
    # API get data
    try:
        city = response['name']
        temp = response['main']['temp']
        description = response['weather'][0]['description']
        wind = response['wind']['speed']
    except KeyError:
        return redirect(url_for('error'))
    return render_template('weather.html',
           city=city, temp=temp, description=description, wind=wind)

@app.route('/')
def weather_search():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)