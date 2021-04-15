#!/usr/bin/env python3

num = int(input())

b = bin(num)
o = oct(num)
h = hex(num)

print(b[2:])
print(o[2:])
print(h[2:].upper())
