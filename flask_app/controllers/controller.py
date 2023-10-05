from flask_app import app
import requests
from flask import render_template, request, redirect, session, flash, jsonify, json
import datetime


@app.route('/')
def landing_page():
    return render_template("index.html")

@app.route('/search')
def weather_search():
    # result = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?zip=98029,us&appid={app.api_key}&units=imperial")
    # return jsonify(result.json())
    
    with open("flask_app/data.json", "r") as read_content: 
        result = json.load(read_content)
        data = {
            'city': result['city']['name'],
            'forecast': []
            
        }
        for i in range(len(result['list'])):
            date = result['list'][i]['dt_txt'].split()[0]
            time = result['list'][i]['dt_txt'].split()[1]
            forecast_data = {
                'date': date,
                'time': time,
                'temp': result['list'][i]['main']['temp'],
                }
            data['forecast'].append(forecast_data)
    return render_template("search_results.html", data=data)
