#Bitwise
a1=0b0011
a2=0b0101
print('a1=0b0011 a2=0b0101')
a3=a1&a2
print('&',a3,bin(a3))
a4=a1|a2
print('|',a4,bin(a4))
a5=a1^a2
print('^',a5,bin(a5))
a6=~a1
print('~',a6,bin(a6))
a7=~(0b0100)
a8=~0b1101
print('~',a7)
print(a8,bin(a8))
