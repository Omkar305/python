a={1,2,3,4,5}
b={3,4,6,7,8,11}
c={3,9,10,11}
print('set a',a)
print('set b',b)
print('set c',c)
print()
print('membership test')
x1=2 in a
print('in',x1)
x2=23 in a
print('in',x2)
print()
print('intersection')
x3=a.intersection(b,c)
print('x3',x3)

print()
print('difference')
x4=a.difference(b,c)
print('x4',x4)
x5=b.difference(a,c)
print('x5',x5)
print()
print('Symmetric difference')
x6=a.symmetric_difference(b)
print('x6',x6)
print()
print('union')
x7=a.union(b,c)
print('x7',x7)

print()
print('add')
print('a',a)
a.add(15)
a.add(20)
print('a',a)

print()
print('copy')
print('a',a)
x8=a.copy()
print('x8',x8)

print()
print('discard')
print('a',a)
a.discard(15)
a.discard(20)
print('a',a)

print()
print('pop')
print('b',b)
x9=b.pop()
print('x9',x9,b)


print()
print('remove')
print('c',c)
c.remove(11)
print('c',c)

























