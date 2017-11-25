#!/usr/bin/env python
num = raw_input('Please input a number: ')
counter = ''

for i in range(int(num)):
    for j in range(int(num)):
        counter = counter+'*'
    
    print counter
    counter = ''
