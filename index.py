import math

def TestMe():
    q = ['how old am I', 'what OS am i using', 'still enjoying test?']
    ans = ['17', 'MacOS', 'yes']
    score = 0
    for i in range(len(q)):
        print (q[i])
        a = input ('answer: \n')
        if a == ans[i]:
            print('niiice')
            score += 1
        else:
            print ('try again')
    
    print (f'You got {score} points')

def Calculator():

    a = input(('Выберите фигуру: \n 1.Квадрат \n 2.Круг \n 3.Прямоугольник \n'))

    #Square
    if a == ('1'):
        first = input(('Чему равна сторона? \n'))
        ans = float(first) ** 2
        print (f'Ответ: {ans}')

    #Circle
    if a == ('2'):
        pi = input ('Округлять число Пи до 3? \n y = да     n = нет \n')
        if pi == ('y'):
            first = input('Чему равен радиус? \n')
            ans = float(first) ** 2 * 3
            print (f'Ответ: {ans}')
        if pi == ('n'):
            first = input(('Чему равен радиус? \n'))
            ans = float(first) ** 2 * math.pi
            print (f'Ответ: {ans}')

    #Rectangle
    if a == ('3'):
        first = input('Чему равна первая сторона? \n')
        second = input('Чему равна вторая сторона? \n')
        ans = float(first) * float(second)
        print (f'Ответ: {ans}')

def Calculator2():
    q = ['Чему равна сторона? \n', 'Чему равен радиус? \n', 'Чему равна первая сторона? \n', 'Чему равна вторая сторона? \n']
    
    a = input(('Выберите фигуру: \n 1.Квадрат \n 2.Круг \n 3.Прямоугольник \n'))
    

    #Square
    if a == ('1'):
        first = input(q[0])
        ans = float(first) ** 2
        print (f'Ответ: {ans}')

    #Circle
    if a == ('2'):
        pi = input ('Округлять число Пи до 3? \n y = да     n = нет \n')
        if pi == ('y'):
            first = input(q[1])
            ans = float(first) ** 2 * 3
            print (f'Ответ: {ans}')
        elif pi == ('n'):
            first = input(q[1])
            ans = float(first) ** 2 * math.pi
            print (f'Ответ: {ans}')
        else:
            error = ('Промахнулся по кнопками походу, дядя')
            print (error)

    #Rectangle
    if a == ('3'):
        first = input(q[2])
        second = input(q[3])
        ans = float(first) * float(second)
        print (f'Ответ: {ans}')
    

Calculator2()