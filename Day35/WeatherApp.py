import requests

weather_dict = {
    'latitude' : 42.473740,
    'longitude' : -83.399070,
    'api' : 'f3c21bb9bf119626cda4ebf4e869dd78'
}

url = 'https://api.openweathermap.org/data/2.5/onecall'

response = requests.get(url, params=weather_dict)
response.raise_for_status()
print(response)
