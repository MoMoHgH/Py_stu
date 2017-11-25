#!/usr/bin/env python
import random

first_name_list = []
first_name  = ''
namelist = []
for i in range(10):
    list = random.sample([chr(i) for i in range(97,123)] , 10)
    for i in range(10):
        first_name = first_name + list[i]
    first_name_list.append(first_name)
    list = []
    first_name = ''
for i in range(10):
    htmlname = first_name_list[i] + '_hgh.html'
    namelist.append(htmlname)
print namelist

