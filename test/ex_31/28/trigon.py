#!/usr/bin/env python
num =int(raw_input('please input a number: '))
counter = ''
for i in range(num):
    for j in range(i+1):
        counter = counter + '*'
    print counter
    counter = ''

