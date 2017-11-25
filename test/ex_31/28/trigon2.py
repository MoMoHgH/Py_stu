#!/usr/bin/env python
num =int(raw_input('please input a number: '))
counter = ''
num1 = num-1
for i in range(num):
    for j in range(num1):
        counter = counter + ' '
    num1 = num1 -1
    for k in range(i+1):
        counter = counter + '*'
    print counter
    counter = ''

