#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
import string
HOST = 'smtp.163.com'
SUBJECT = '123'
FROM = 'hgh_da@163.com'
TO = '1418803468@qq.com'
text = "你是笨蛋"
BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT,
        "",
        text
        ),"\r\n")
server = smtplib.SMTP()
server.connect(HOST,"25")
server.starttls()
server.login("hgh_da@163.com","252487559.s")
server.sendmail(FROM,[TO],BODY)
server.quit()
