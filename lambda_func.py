#!/usr/bin/env python
#coding : utf-8
import math
def calc(s):

	if s =='+':
		return lambda a,b: a+b
	if s =='*':
		return lambda a,b:a*b
	if s == '/':
		return lambda a,b:a/b
	else:
		assert False,"error: operator not define"

calc_dict={
	'+':lambda a,b :a+b,
	'*':lambda a,b:a*b,
	'/':lambda a,b:a/b,
}

if __name__ == '__main__':
	a,b,c,d = 1,2,3,4

	print calc_dict['*'](100,100 )
	##print calc('-')(calc('*')(calc('+')(a,b),c),d)