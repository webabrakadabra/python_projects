#!/usr/bin/env python3

import random

DIGITS  = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'



def passw_number():
    while True:
        passw_number = input('Введите количество паролей для генерации: ')
        if passw_number.isdigit() and int(passw_number) > 0:
            return int(passw_number)
        else:
            print('Ошибка!')

def passw_len():
    while True:
        passw_len = input('Введите длину одного пароля: ')
        if passw_len.isdigit() and int(passw_len) > 0:
            return int(passw_len)
        else:
            print('Ошибка!')

def passw_is_digit():
    while True:
        passw_is_digit = input('Включать ли цифры 0123456789? Y - да, N - нет: ')
        if passw_is_digit == 'Y' or passw_is_digit == 'y':
            return True
        elif passw_is_digit == 'N' or passw_is_digit == 'n':
            return False
        else:
            print('Ошибка!')

def passw_is_big_letters():
    while True:
        passw_is_big_letters = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Y - да, N - нет: ')
        if passw_is_big_letters == 'Y' or passw_is_big_letters == 'y':
            return True
        elif passw_is_big_letters == 'N' or passw_is_big_letters == 'n':
            return False
        else:
            print('Ошибка!')

def passw_is_little_letters():
    while True:
        passw_is_little_letters = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Y - да, N - нет: ')
        if passw_is_little_letters == 'Y' or passw_is_little_letters == 'y':
            return True
        elif passw_is_little_letters == 'N' or passw_is_little_letters == 'n':
            return False
        else:
            print('Ошибка!')

def passw_is_symbols():
    while True:
        passw_is_symbols = input('Включать ли символы !#$%&*+-=?@^_? Y - да, N - нет: ')
        if passw_is_symbols == 'Y' or passw_is_symbols == 'y':
            return True
        elif passw_is_symbols == 'N' or passw_is_symbols == 'n':
            return False
        else:
            print('Ошибка!')

def passw_is_amb_symbols():
    while True:
        passw_is_amb_symbols = input('Исключать ли неоднозначные символы il1Lo0O? Y - да, N - нет: ')
        if passw_is_amb_symbols == 'Y' or passw_is_amb_symbols == 'y':
            return True
        elif passw_is_amb_symbols == 'N' or passw_is_amb_symbols == 'n':
            return False
        else:
            print('Ошибка!')
    
def symbols():
    chars = ''
    if passw_is_digit():
        chars += '0123456789'
    if passw_is_big_letters():
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if passw_is_little_letters():
        chars += 'abcdefghijklmnopqrstuvwxyz'
    if passw_is_symbols():
        chars += '!#$%&*+-=?@^_'
    if passw_is_amb_symbols():
        chars = chars.replace('i', '')
        chars = chars.replace('l', '')
        chars = chars.replace('1', '')
        chars = chars.replace('L', '')
        chars = chars.replace('o', '')
        chars = chars.replace('0', '')
        chars = chars.replace('O', '')

    return chars

def generate_password(passw_number, passw_len, symbols):
    for _ in range(passw_number):
        passw = ''
        for _ in range(passw_len):
            passw += random.choice(symbols)
        print(passw)

generate_password(passw_number(),passw_len(), symbols())


