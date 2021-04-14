#!/usr/bin/env python3
'''
val = input('Шифровать или дешифровать? E - шифровать, D - дешифровать')
lang = input('Укажите язык алфавита. R - русский, E - английский')
key = int(input('Введите число шага сдвига'))
'''
def encrypt(lang, key, string):
    newstring = ''
    if lang == 'R':
        for i in range(len(string)):
            x = ord(string[i])
            if 1040 <= x <= 1071:
                x = ((x - 1040) + key) % 32
                newstring += chr(x + 1040)
                #print(x)
            elif 1072 <= x <= 1103:
                x = ((x - 1072) + key) % 32
                newstring += chr(x + 1072)
                #print(newstring)
            else:
                newstring += chr(x)
        print(newstring)
            
    elif lang == 'E':
        pass
    else:
        print('Укажите язык алфавита!!! R - русский, E - английский')

    
def decrypt(lang, key, string):
    pass
    
    


encrypt('R', 10, 'Блажен, кто верует, тепло ему на свете!')
