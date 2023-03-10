from . import keys
import requests

# returns JSON with temp, humidity, and condition
def getWeather()->dict:
    url = "http://api.weatherapi.com/v1/current.json"
    params = {"key" : keys.weatherKey, 'q': "State College"}

    try:
        response = requests.get(url, params=params)
    except:
        print('Connection to weather API failed')
        return -1
    if response.status_code != 200:
        return response.status_code
    
    data = response.json()

    return {'Temp': data['current']['temp_f'], 'Humidity': data['current']['humidity'],
            'Condition':data['current']['condition']['text']}