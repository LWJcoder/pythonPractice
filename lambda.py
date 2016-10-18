#!/usr/bin/env python
#coding : utf-8

import random

def fil():
	a = "a8dcd9S9HDJJ2JDJ009fkJJH"
	b = list(filter(str.isalpha,a))
	c = sorted(b,lambda x,y:1 if (x.upper()>y.upper()) else -1 ,reverse = False)
	#### change the list如果大写x >y,返回1，否则返回-1
	b.sort(lambda x,y:1 if (x.upper()>y.upper()) else -1 , reverse = False)

	print ''.join(c)
	print ''.join(b)
if __name__ == '__main__':
	fil()




	
	#lst = random.randint(-50,50)

	#lst2 = filter(lambda n: n>0, lst)

	#lst3 = map(lambda n:n*2,lst)
	#lst4 = reduce(fil,lst3)
