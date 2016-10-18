##爬百度百科的链接
import urllib
from bs4 import BeautifulSoup
import re

html = urllib.urlopen('http://baike.baidu.com/view/284853.htm')
bs_obj = BeautifulSoup(html,"html.parser")

#a_list = bs_obj.find("a",href=re.compile("baike\.baidu\.com\/view\/284853\.htm"))
a_list = bs_obj.findAll("a")

for aa in a_list:
	if not aa.find("img"):
		if aa.attrs.get('href'):
			print aa.text,aa.attrs['href']
