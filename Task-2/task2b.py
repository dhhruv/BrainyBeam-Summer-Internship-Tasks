s = {22, 55, 11, 66, 33}
print(s)

s.add(44)  # inserts the specified element in set
print(s)

c = {11, 44, 77, 88, 99}
t = s.union(c)  # returns the union of given set
print(t)

q = s.intersection(c)  # returns the intersection of the given set
print(q)

w = s.difference(c)  # returns the difference of the given set
print(w)

w.clear()  # clears the contents of the given set
print(w)
