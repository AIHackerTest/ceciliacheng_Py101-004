#在1~20之间猜数字
#玩家一共有4次机会尝试

import random

print('\n请在1~20之间猜一个数字，你一共有4次机会。')

sysNum = random.randint(1,20) #随机数字
countTimes = 0 #计算玩家输了多少次的容器

while True:
    try:
        userInput = int(input('> '))

        if (userInput > 20 or userInput<1):
            print('超出范围了！')
            break

        if userInput == int(input('> ')):
            print('请输入数字！')
            break

        if(userInput < sysNum and countTimes < 4):
            countTimes += 1
            print('小了，你还有{}次机会'.format(int(4-countTimes)))

        elif(userInput > sysNum and countTimes < 4):
            countTimes += 1
            print('大了，你还有{}次机会'.format(int(4-countTimes)))

        elif(userInput == sysNum):
            countTimes += 1
            print('Bingo!你猜中了，你一共猜了{}次'.format(int(countTimes)))
            break

        if (countTimes >= 4):
            print('超过4次，game over。')
            break

    except ValueError:
        print('你输入的不是数字，请重新输入！')
