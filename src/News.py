from . import keys
import requests

def getNews()->dict:
    url = 'https://newsapi.org/v2/top-headlines?'
    params = {'country': 'us','apiKey': keys.newsKey}
    
    response = requests.get(url, params=params)
    
    if response.status_code !=200:
        return response.status_code

    data = response.json()

    result = []

    for i in range(3):
        result.append(data['articles'][i]['title'])
    
    return result