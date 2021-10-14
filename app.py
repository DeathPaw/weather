import requests
import time
import json
import os
import numpy as np
from datetime import date, timedelta
from flask import Flask, render_template, request

api_key = os.environ['API_KEY']
app = Flask(__name__)


@app.route('/')
def weather_dashboard():
    return render_template('home.html')

@app.route("/weather")
def weather():
    print("hi")
    city = request.args.get('city')
    days_number = int(request.args.get('days'))  
    response = calculate_result(city, days_number)
    print(response)
    return response

@app.route('/output', methods=['POST'])
def test1():
    
    days_number = request.form['days_number']
    city = request.form['city']     
    response = calculate_result(city, days_number)
    return my_json

def get_weather(today, end_date, api_key, city):
    url = "https://visual-crossing-weather.p.rapidapi.com/history"
    request_start_date = str(today)+"T00:00:00"
    request_end_date = str(end_date)+"T00:00:00"
    querystring = {"startDateTime":request_end_date,
                   "aggregateHours":"24",
                   "location":city,
                   "endDateTime":request_start_date,
                   "unitGroup":"us",
                   "dayStartTime":"8:00:00",
                   "contentType":"json",
                   "dayEndTime":"17:00:00",
                   "shortColumnNames":"0"}

    headers = {
        'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com",
        'x-rapidapi-key': api_key
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

def calculate_result(city, days_number):
    today = date.today()
    end_date = today - timedelta(days=int(days_number))
    data = get_weather(today, end_date, api_key, city)
    day=0
    humidity=[day]*int(days_number)
    temp=[day]*int(days_number)
    sealevelpressure=[day]*int(days_number)
    for day in range(int(days_number)):
        humidity[day] = float("{0:.2f}".format(data["locations"][city]["values"][day]["humidity"]))
        temp[day] = float("{0:.2f}".format(data["locations"][city]["values"][day]["temp"]))
        sealevelpressure[day] = float("{0:.2f}".format(data["locations"][city]["values"][day]["sealevelpressure"]))
    location = data["locations"][city]["tz"]
        
    #РЕКВЕСТ СЕМАНТИЧЕСКИ
    ###JSON ENDPOINT
    res={
        "city": location,
         "from": str(end_date),
         "to": str(today),
         "temperature_F": {
             "average": np.average(temp),
             "median": np.median(temp),
             "min": np.min(temp),
             "max": np.max(temp) },
         "humidity": {
             "average": np.average(humidity),
             "median": np.median(humidity),
             "min": np.min(humidity),
             "max": np.max(humidity) },
         "pressure_mb": {
             "average": np.average(sealevelpressure),
             "median": np.median(sealevelpressure),
             "min": np.min(sealevelpressure),
             "max": np.max(sealevelpressure) }
         }
    return res


if __name__ == '__main__':
    app.run()
