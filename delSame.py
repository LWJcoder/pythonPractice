l1 = ["a", "c", "a", "a", "b"]
l2 = []
[l2.append(i) for i in l1 if not i in l2]
print l2
