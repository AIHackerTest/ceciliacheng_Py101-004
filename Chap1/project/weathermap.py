with open('weather_info.txt') as file:
    list = file.read().split("\n")

dict = {} #初始化存放天气的字典
for i in list:
    if (i!= ""):
        dict[i.split(',')[0]] = i.split(',')[1]
#print(dict)

his = [] #初始化存放查询历史的列表

while True:
    option = input("您好，如需查询天气，请输入城市名称，如需帮助请输入'help'。如需退出请输入'quit'。\n")

    if option in dict.keys():
        print("您查询的{0}的天气状况是{1}".format(option, dict[option]))
        his.append(option+":"+dict[option])

    elif option == "help":
        print("""
            > 请输入城市名称,获取该城市的天气信息;
            > 请输入history,获取历史查询信息;
            > 请输入help,获取帮助信息;
            > 请输入quit,退出该程序;
            """)

    elif option == "history":
        if len(his) == 0:
            print("暂无查询记录，请输入help寻求帮助或再输入其他城市。")
        else:
            print(his)

    elif option == "quit":
        print("谢谢您的信任，欢迎再次使用我们的服务。")
        exit(0)
    else:
        print("查无此城市,请输入help寻求帮助或输入其他城市。")
