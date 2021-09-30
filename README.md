# List of needed data
* Temperature
  -   minimum temperature
  -   maximum temperature
  -   middle temperature
  -   median temperature
* Preccure
  -   maximum preccure
  -   minimum preccure
  -   middle preccure
  -   median preccure
* Humidity
  -   maximum humidity
  -   minimum humidity
  -   middle humidity
  -   median humidity
---
# Example of Json    
    {  
      "city": "Saint-Petersburg",  
      "from": "2021-09-10",  
      "to": "2021-09-15",  
      temperature_c": {  
        "average": 25.0,  
        "median": 24.5,  
        "min": 20.1,  
        "max": 29.3  
        },  
      "humidity": {  
        "average": 55.4,  
        "median": 58.1,  
        "min": 43.1,  
        "max": 82.4  
       },  
      "pressure_mb": {  
        "average": 1016.0,  
        "median": 1016.5,  
        "min": 1015.1,  
        "max": 1017.3  
      }  
    }  
# Params of request
* City
* Number of days to analyze
# Request
Service receives GET requests
    /weather?city=<city>&days=<n>
  ---
# Docker
* Start on local Linux machine 
           docker build [PATH_TO_DOCKERFILE] -t weather       
           docker run -p 8080:8080 -e API_KEY=[YOUR_API_KEY] weather        
  
* Or you can pull image from Dockeer Hub  
       docker pull tenaciousfoxy/weather        
           docker run -p 8080:8080 -e API_KEY=[YOUR_API_KEY] weather             
