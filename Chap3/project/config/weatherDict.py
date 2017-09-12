import requests
import json

option = input('>>> ')

def fetchWeather(option):
    url_API = 'https://api.seniverse.com/v3/weather/now.json?'

    result = requests.get(url_API, params={
        'key': '8xejamoxtxft88qo',
        'location': option,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=20)

    info = json.loads(result.content)
    weatherdict = {}
    weatherdict['city'] = info['results'][0]['location']['name']
    weatherdict['weather Condiction'] = info['results'][0]['now']['text']
    weatherdict['weather Temperature'] = info['results'][0]['now']['temperature']
    weatherdict['Time']=info['results'][0]['last_update']
    return weatherdict

fetchWeather(option)
