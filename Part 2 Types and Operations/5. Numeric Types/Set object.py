print('set object')
s1={1,2,3,4,5}
print(s1)
s2={4,5,6,7}
print(s2)
s3=s1 | s2
print('union',s3)
s4=s1.union(s2)
print('union',s4)
s5=s1 & s2
print('intersection',s5)
s6=s1.intersection(s2)
print(s6)
s7=s1-s2
print('set difference',s7)
s8=s2-s1
print('set difference',s8)
s9=(s1-s2)| (s2-s1)
print(s9)
