#!/usr/bin/env python3
# объявление функции

import random

x = random.randint(1, 100)
total = 0
z = 100
print('Добро пожаловать в числовую угадайку')


def is_valid(n):
    if n.isdigit() and 1 <= int(n) <= z:
        return True
    else:
        return False

while True:
    n = input('Введите число: ')
    if is_valid(n) and x > int(n):
        total += 1
        print('Ваше число меньше загаданного, попробуйте еще разок \n')
    elif is_valid(n) and x < int(n):
        total += 1
        print('Ваше число больше загаданного, попробуйте еще разок \n')
    elif is_valid(n) and x == int(n):
        print('Вы угадали, поздравляем!')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        print('Попыток:', total)
        print('Ёще разок? Нажмите Y - да, N - нет')
        g = input()
        if g == 'Y' or g == 'y':
            total = 0
            print('ВВедите границу отгадываемого числа: ')
            z = int(input())
            x = random.randint(1, z)
        elif g == 'N' or g == 'n':
            break
        else:
            print('Нажмите Y - да, N - нет')
    else:
        print('А может быть все-таки введем целое число от 1 до', str(z) + '?')

