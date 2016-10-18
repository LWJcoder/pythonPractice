# coding: utf-8
import codecs
f = codecs.open('file_ch.txt','w','utf-8')

f.write(u'y哦那个\n')
f.write(u'一定是傻了\n')
f.write(u'云课堂\n')

f.close()

#read file
f = codecs.open('file_ch.txt','r','utf-8')
print f.read(1)
print f.readline()
print f.readline()
print f.readline()
f.close()

import os
print os.path.exists('file_ch.txt')
#os.rename('file_ch','file')
#print os.exists('file_ch.txt')

import shelve

d = shelve.open('file.shelve')
d['qq'] = 'www.qq.com'
d.close()


import cPickle
obj = {'qq':'djkhjd'}
f = open('file_ch.txt','utf-8')
cPickle.dump(obj,f)
f.close()


obj_r = cPickle.load(f)
print obj_r