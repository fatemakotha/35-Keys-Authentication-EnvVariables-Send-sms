import requests

MY_CITY = "Dhaka"
DHAKA_LAT = "23.810331"
DHAKA_LNG = "90.412521"
api_key = "11407c01a394cbe33f6eb425251bee48"

#For One Call Api plan:
OpenWeatherMap_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

response = requests.get(url=, params=MY_CITY)
response.raise_for_status()

data = response.json()
print(data)

