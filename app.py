import requests
import configparser
import time
import json
import numpy as np
from datetime import date, timedelta
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def weather_dashboard():
    return render_template('home.html')

@app.route('/output', methods=['POST'])
def test1():
    today = date.today()
    days_number = request.form['days_number']
    city = request.form['city']
    end_date = today - timedelta(days=int(days_number))
    #print (city)
    #print (days_number)
    api_key = get_api_key()
    data = get_weather(today, end_date, api_key, int(city))
       
    day=0
    humidity=[day]*int(days_number)
    temp=[day]*int(days_number)
    sealevelpressure=[day]*int(days_number)
    #return data
    for day in range(int(days_number)):
        humidity[day] = float("{0:.2f}".format(data["locations"][city]["values"][day]["humidity"]))
        temp[day] = float("{0:.2f}".format(data["locations"][city]["values"][day]["temp"]))
        sealevelpressure[day] = float("{0:.2f}".format(data["locations"][city]["values"][day]["sealevelpressure"]))
    location = data["locations"][city]["tz"]
        
    med_temp=np.median(temp)
    avg_temp=np.average(temp)
    min_temp=np.min(temp)
    max_temp=np.max(temp)

    med_humidity=np.median(humidity)
    avg_humidity=np.average(humidity)
    min_humidity=np.min(humidity)
    max_humidity=np.max(humidity)

    med_pressure=np.median(sealevelpressure)
    avg_pressure=np.average(sealevelpressure)
    min_pressure=np.min(sealevelpressure)
    max_pressure=np.max(sealevelpressure)
    ###JSON ENDPOINT
    res={"city": location, "from": str(end_date), "to": str(today), "temperature_F": { "average": avg_temp, "median": med_temp, "min": min_temp, "max": max_temp },
         "humidity": { "average": avg_humidity, "median": med_humidity, "min": min_humidity, "max": max_humidity },
         "pressure_mb": {"average": avg_pressure, "median": med_pressure, "min": min_pressure, "max": max_pressure } }
    my_json=json.dumps(res)
    #print (my_json)
    ###MY ENDPOINT
    #return render_template('weather.html',
    #                       location=location, temp=temp,
    #                       humidity=humidity, sealevelpressure=sealevelpressure, start_date = end_date, end_date = today)
    return my_json

def get_weather(today, end_date, api_key, city):
    url = "https://visual-crossing-weather.p.rapidapi.com/history"
    request_start_date = str(today)+"T00:00:00"
    request_end_date = str(end_date)+"T00:00:00"
    querystring = {"startDateTime":request_end_date,"aggregateHours":"24","location":int(city),"endDateTime":request_start_date,"unitGroup":"us","dayStartTime":"8:00:00","contentType":"json","dayEndTime":"17:00:00","shortColumnNames":"0"}

    headers = {
        'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com",
        'x-rapidapi-key': api_key
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['x-rapidapi-key']


if __name__ == '__main__':
    app.run()
