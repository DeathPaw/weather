from flask import Flask

app = Flask(__name__)
import requests

url = "https://visual-crossing-weather.p.rapidapi.com/history"

querystring = {"startDateTime":"2019-01-01T00:00:00","aggregateHours":"1","location":"Washington,DC,USA","endDateTime":"2019-01-03T00:00:00","unitGroup":"us","dayStartTime":"8:00:00","contentType":"json","dayEndTime":"17:00:00","shortColumnNames":"0"}

headers = {
    'x-rapidapi-host': "visual-crossing-weather.p.rapidapi.com",
    'x-rapidapi-key': "d3ef335d75mshbe199c803c0737bp1762b0jsn8bad9be113ee"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
@app.route("/")
def hello_world():
    return response.text
