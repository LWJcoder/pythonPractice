#coding: utf-8

from bs4 import BeautifulSoup
import urllib
import re

url = 'http://www.heibanke.com/lesson/crawler_ex00/'


html = urllib.urlopen(url)
bs_obj = BeautifulSoup(html, "html.parser")

#find h3
h3tag = bs_obj.find("h3").text
print h3tag
num = re.findall(r'/\d+/',h3tag)

print num.group()
   


