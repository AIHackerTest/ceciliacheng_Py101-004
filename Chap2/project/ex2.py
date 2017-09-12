import requests
import json

def helplist():
    print("""
        > 请输入城市名称,获取该城市的天气信息;
        > 请输入history,获取历史查询信息;
        > 请输入help,获取帮助信息;
        > 请输入quit,退出该程序;
        """)

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

his = []

while True:
    option = input('您好，如需查询天气，请输入城市名称，如需帮助请输入help。如需退出请输入quit。\n')
    if option == 'help':
        helplist()
        continue
    elif option == 'history':
        if len(his) == 0:
            print("暂无查询记录，请输入help寻求帮助或再输入其他城市。")
        else:
            for i in his:
                print(i)
    elif option == 'quit':
        print("谢谢您的信任，欢迎再次使用我们的服务。")
        exit(0)
    else:
        option = fetchWeather(option)
        displayToUser = (option['city'] + '现在的天气是:' +
            option['weather Condiction'] + ', ' + option['weather Temperature']
            +'摄氏度,' + option['Time'])
        print(displayToUser)
        his.append(displayToUser)
