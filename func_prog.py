#coding :utf-8
import random

s = " @2345il03i33k23e65p65y623t65h62o23n32"
print filter(str.isalpha,s)


print "##############################"
l = [random.randint(0,100) for i in range(10)]
def sub50(a):
	return a-50

print l
print map(sub50,l)
print "##############################"
#REDUCE
import math
def  f_add(a,b):
	return a+b
def f_mul(a,b):
	return a*b
def f_sqrt(a,b):
	x =  math.sqrt(float(a+b))
	print x*x
	return x
print reduce(f_add,range(1,100))
print reduce(f_sqrt,range(1,100))
print reduce(f_mul,range(1,100))