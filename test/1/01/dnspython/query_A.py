#!/usr/bin/env python
import dns.resolver

domian = raw_input('please input an domian: ')
A = dns.resolver.query(domian , 'A')
for i in A.response.answer:
    print i
    for j in i.items:
        print j

