# Dell weather service
now returns Json historical weather for Washington by hours, from 2019-01-01 till 2019-01-03.
# TODO
* Selecter to choose city(after user choose needed one we should define latitude and longitude, so call GET request with that)
* Parse Json(now it just print, looks really bad), need to create the HTML index.html to use variables from the context dictionary.
* Aggrigate data and return needed only (calculate median/middle, search for maximum/minimum)
# List of needed data
* Temperature
  -   minimum temperature
  -   maximum temperature
  -   middle temperature
  -   median temperature
* Preccure
  -   maximum preccure
  -   minimum preccure
* Humidity
  -   maximum humidity
  -   minimum humidity
---
# Params of request
* City
* Number of days to analyze
