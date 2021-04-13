#!/usr/bin/env python3

import random

DIGITS  = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'

chars = ''
passw_number = int(input('Введите количество паролей для генерации: '))
passw_len = int(input('Введите длину одного пароля: '))
passw_is_digit = input('Включать ли цифры 0123456789 ? Y - да, N - нет: ')
passw_is_big_letters = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Y - да, N - нет: ')
passw_is_little_letters = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Y - да, N - нет: ')
passw_is_symbols = input('Включать ли символы !#$%&*+-=?@^_? Y - да, N - нет: ')
passw_is_amb_symbols = input('Исключать ли неоднозначные символы il1Lo0O? Y - да, N - нет: ')
