test = -1

def check_int(n):
    try:
        n = int(n)
        return n
    except ValueError:
        return ''

less = [
'1  - Найти кубы чисел от 1 до N.',
'2  - Подсчитать сумму цифр в числе.',
'3  - Написать программу вычисления произведения чисел от 1 до N.',
'4  - Показать кубы чисел, заканчивающихся на четную цифру.',
'0  - Выход.'
]

for i in range(len(less)):
    print(less[i])
print('')

def in1():
    print(less[0])
    n = input("Введите число кубических чисел: ")
    if (check_int(n) != ""):
        n= int(n)
        counter = 1
        while counter <= n:
            print(counter ** 3)
            counter += 1
    else:
        print ("Введено не число")

def in2():
    print(less[1])
    n=input("Введите число: ")
    summ_n = 0
    if (check_int(n) !=""):
        for i in range(len(n)):
                summ_n = summ_n + int(str(n[i]))
        print ("Сумма числе: ", summ_n)
    else:
        print ("Введено не число")

def in3():
    print(less[2])
    n = input("Введите число: ")
    if (check_int(n) != ""):
        summ_n = 0
        for i in range(int(n)):
            summ_n = summ_n + (i+1)
        print ("произведение чисел: ", summ_n)
    else:
        print("Введено не число")

def in4():
    print(less[3])
    n = input("Введите число кубических чисел: ")
    if (check_int(n) != ""):
        n = int(n)
        counter = 1
        countercub = 1
        while countercub <= n:
            if ((counter ** 3) % 2) == 0:
                print(counter ** 3)
                countercub += 1
                counter += 1
            else:
                counter += 1
    else:
        print ("Введено не число")

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