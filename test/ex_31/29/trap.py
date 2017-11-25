#!/usr/bin/env python

num1,num2 = (int(x) for x in raw_input( \
    'please input num1 and num2 : ').split(' '))
counter = ''
if num2 > num1:
    num3 = num2-num1+1
    for i in range(num3):
        for j in range(num1):
            counter = counter + '*'
        print counter
        counter = ''
        num1 = num1 +1

elif num2 < num1:
    num3 = num1-num2+1
    for i in range(num3):
        for j in range(num1):
            counter = counter + '*'
        print counter
        counter = ''
        num1 = num1 -1
else:
    print 'num1 can\'t eq num2'
