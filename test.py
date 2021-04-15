#!/usr/bin/env python3
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

x = keys('Day, mice. "Year" is a mistake!')

print(x[0])
