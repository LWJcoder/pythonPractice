a = [1,2,3]
a_ref = a
a_copy = a[:]

print str(a_copy)

a.pop()
print "pop" + str(a)
a.insert(1,100)
print "insert"+str(a)
a.sort()
a.reverse()


