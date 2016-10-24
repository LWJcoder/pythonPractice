#!/usr/bin/env python    
# -*- coding: utf-8 -*- 

import requests



url = 'http://www.heibanke.com/lesson/crawler_ex01/'

psw = 0

while(psw <= 30):
    params = {'username': 'heibanke', 'password':str(psw)}
    r = requests.post(url,data = params )
    if r.text.find(u'输入的密码错误')>0:
        psw += 1
    else:
        print r.text
        break;


