#!/usr/bin/env python3

text = input()

def keys(string):
    
    string = string.split(' ')
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = []

    for i in range(len(string)):
        count = 0
        for k in range(len(string[i])):
            if string[i][k] in alphabet:
                count += 1
        key.append(count)

    return key

def encrypt(string):

    key = keys(string)
    string = string.split(' ')
    newmas = []
    
    for i in range(len(string)):
        newstring = ''
        for k in range(len(string[i])):
            x = ord(string[i][k])
            if 65 <= x <= 90:
                x = ((x - 65) + key[i]) % 26
                newstring += chr(x + 65)
            elif 97 <= x <= 122:
                x = ((x - 97) + key[i]) % 26
                newstring += chr(x + 97)
            else:
                newstring += chr(x)
        newmas.append(newstring)
    print(' '.join(newmas))

encrypt(text)
