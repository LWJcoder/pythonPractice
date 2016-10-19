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
		self.__owner = owner

		assert length>0,"length must large than 0"
		self._length = length
		self._height = height
		self._width = width
	
	def getOwner(self):
		return self.__owner

	def setOwner(self, value):
		self.__owner = value

	def setLength(self, value):
		assert value>0,"length must large than 0"
		self._length = value

	def getLength(self):
		return self._length

if __name__ == '__main__':
	a = car(1,2,4,u'小黑')
	print a.getOwner()

	print dir(a)
	#a.setLength(-1)