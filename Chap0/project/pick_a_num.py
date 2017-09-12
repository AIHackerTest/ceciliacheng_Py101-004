#我构想的猜数字游戏是：玩家猜的数字范围是在1~20之间，
#每次猜错都会缩小数字范围

import random

def sys_num():
    defaultNum = random.randint(1,21) #随机生成随机数字，玩家猜中这个数字的话，游戏会退出
    return defaultNum

def user_num():
    userInput = int(input('请猜一个在1~20之间的数字。'))
    return userInput

def binsearch(guessRange,userInput,left,right):
    left = 1
    right = 21
    guessRange = list(range(left,right))

    while（left <= right):
        if(userInput > defaultNum): #玩家输入的数字比系统生成的数字大
            right = userInput
            guessRange = list(range(left,right))
            print('请在{}到{}之间猜数字'.format(left,userInput))

        elif(userInput < defaultNum):
            left = userInput  #玩家输入的数字比系统生成的数字小
            guessRange = list(range(left,right))
            print('请在{}到{}之间猜数字'.format(userInput,right))

        elif(userInput < left) or (userInput > right): #预防机制：防止玩家输入的数字比范围大
            print('超过范围啦，重新在{}到{}之间猜数字啦'.format(left,right))

        elseuserInput == defaultNum: #玩家猜中数字，游戏结束
            print ('Bingo! You win!')
            break

print（binsearch）
