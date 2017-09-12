from flask import Flask, render_template, request
from weatherDict import fetchWeather

app = Flask(__name__) #Flask固定要求
his = []

@app.route('/')
def index():
    return render_template('index.html') #在Flask里寻找模板

@app.route('/user_request', methods=["GET", "POST"])
def web_request():
    info = request.args.get('city') #获取查询城市的天气资料
    try:
        weather_display = fetchWeather(info)
        his.append(weather_display)
        return render_template('query.html',weather_display=weather_display)
    except KeyError:
        if request.args.get('history') == '历史':
            return render_template('history.html',his=his)

        elif request.args.get('help') == '帮助':
            return render_template('help.html')

        else:
            return
            # return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
