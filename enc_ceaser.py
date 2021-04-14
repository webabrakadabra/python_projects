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
        for i in range(len(string)):
            x = ord(string[i])
            if 65 <= x <= 90:
                x = ((x - 65) + key) % 26
                newstring += chr(x + 65)
                #print(x)
            elif 97 <= x <= 122:
                x = ((x - 97) + key) % 26
                newstring += chr(x + 97)
                #print(newstring)
            else:
                newstring += chr(x)
        print(newstring)
    else:
        print('Укажите язык алфавита!!! R - русский, E - английский')

    
def decrypt(lang, key, string):
    pass
    
    


encrypt('E', 17, 'To be, or not to be, that is the question!')
