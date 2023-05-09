print('Set Object')
a1={3,4,5,6,7}
print(a1)
a2={6,7,8,9}
print(a2)
a3=a1 | a2
print('Union', a3)
a4=a1 & a2
print('Intersection', a4)
a5=a1 - a2
print('Set difference', a5)
a6=a2 - a1
print('Set difference', a6)
a7=(a1 - a2) | (a2 - a1)
print('Set Symmetric', a7)

