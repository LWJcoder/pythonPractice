import list

a = [1,2,3]
a_ref = a
 
a_ref[2] = 100

a.append(300)

a_copy = a[:]

a.insert(1,50)

a.sort()

a.pop()

a.reverse()

del a[0]


print a[2]
print a_ref[2]

C = [a,a_ref]
print C

b = a+(100,200)

d = a*2

#元组
t = tuple(a)

print t

t.count(3)

t+(1,2)