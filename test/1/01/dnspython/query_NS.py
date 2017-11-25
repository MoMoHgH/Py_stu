#!/usr/bin/env python

import dns.resolver

domain = raw_input('>>>please input an domain:')

NS = dns.resolver.query(domain , 'NS')
for i in NS.response.answer:
    for j in i.items:
        print j
