#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf8') 

class car(object):
	#new class
	"""this is class car"""
	country = u'中国'
	def __init__(self, length,width,height,owner=None):
		self.owner = owner
		self.length = length
		self.height = height
		self.width = width
		self.country = "china"


if __name__ == '__main__':
	a = car(1,2,4,u'小黑')
	b = car(2,5,1,u'辛晓琪')
	print a.owner
	print b.owner
	print a.country
	print b.country

	b.country = u'美国'

	print"******************"
	print a.country
	print b.country
	print car.country

	del a.country
	print a.country



