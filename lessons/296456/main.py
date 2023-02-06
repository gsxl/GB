from random import randint
from math import sqrt

test = -1

def check_int(n):
    try:
        n = int(n)
        return n
    except ValueError:
        return ''

print('1  - Найти кубы чисел от 1 до N.')
print('2  - Подсчитать сумму цифр в числе.')
print('3  - Написать программу вычисления произведения чисел от 1 до N.')
print('4  - Показать кубы чисел, заканчивающихся на четную цифру.')
print('0  - Выход.')
print('')

def in1():
    print('1  - Дано число обозначающее день недели. Выяснить является номер дня недели выходным.')
    in1 = input("Веедите номер дня недели, от 1 до 7 включительно: ")
    if (check_int(in1) != "" and len(in1) ==1 and int(in1)> 0 and int(in1)< 8):
        weekday = ['бездельник,','повторник,','бреда,','чертегдерг,','расслабильница,','клуббота,','высплюсенье,']
        if (int(in1) >= 6):
            w = "и это выходной ;)"
        else:
            w = "но боюсь, что это не выходной :("
        print ("Выбран", in1, "день недели, это:", weekday[int(in1)-1], w, sep=" ")
    else:
        print ("На неделе у Вас что-то пошло не так!")

def in2():
    print('2  - По двум заданным числам проверять является ли одно квадратом другого.')
    in2 = input("Веедите через пробел 2 числа: ")
    in2 = in2.split()
    if (len(in2) >1 and check_int(in2[0]) !="" and check_int(in2[1]) !="" ):
        in2[0] = int(in2[0])
        in2[1] = int(in2[1])
        if (in2[0] / in2[1] == in2[1] or in2[1] / in2[0] == in2[0]):
            if(in2[0] / in2[1] == in2[1]):
                print(in2[0], "является квадратом", in2[1])
            else:
                print(in2[1], "является квадратом", in2[0])
        else:
            print("Оба числа не являются квадратом друг друга.")
    else:
        print ("Вы ввели не 2 числа, или введены не числа")

def in3():
    print('3  - Задать номер четверти, показать диапазоны для возможных координат.')
    in3 = input("Введите номер четверти: ")
    xy = ['x > 0, y > 0', 'x < 0, y > 0', 'x < 0, y < 0', 'x > 0, y < 0']
    if (check_int(in3) != ""):
        print("Координат(ы) в области ", xy[int(in3)-1])
    else:
        print ("Введено не число!")

def in4():
    print('4  - Найти расстояние между точками в пространстве 2D/3D.')
    min = -10
    max = 10

    t1x = randint(min, max)
    t1y = randint(min, max)
    t1z = randint(min, max)

    t2x = randint(min, max)
    t2y = randint(min, max)
    t2z = randint(min, max)

    print ("Точка 1:", "x:", t1x, "y:",t1y, "z:",t1z, sep=" ")
    print ("Точка 2:", "x:", t2x, "y:", t2y, "z:", t2z, sep=" ")

    d = (t2x-t1x)**2+(t2y-t1y)**2+(t2z-t1z)**2

    print("Расстояние между точками: ", sqrt(d))

while test == -1:
    print()
    hw = input('Введите вариан ДЗ: ')
    if check_int(hw) !='' and int(hw) >-1 and int(hw) <12:

        if int(hw) == 1:
            in1()
        elif int(hw) == 2:
            in2()
        elif int(hw) == 3:
            in3()
        elif int(hw) == 4:
            in4()
        elif int(hw) == 0:
            print ("Пока, пока!!!")
            test = 0