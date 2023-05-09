a={11,12,13,14,15}
b={13,14,15,16,17,18,19}
c={13,14,20,21,22}
print('Set a',a)
print('Set b',b)
print('Set c',c)
print()


x1=a.intersection(b,c)
print('intersection',x1)

x2=a.union(b,c)
print('union',x2)

x3=a.difference(b,c)
print('difference',x3)

x4=a.symmetric_difference(b)
print('symmetric difference',x4)

x5=a.symmetric_difference(c)
print('symmetric difference',x5)


