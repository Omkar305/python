#Unpacked argument

def f8(a,b,c,d):
    print('a:',a)
    print('b:',b)
    print('c:',c)
    print('d:',d)

f8(*(1,2,3,4))
f8(**{'a':1,'b':2,'c':3,'d':4})
f8(1,*(5,6),**{'d':80})
f8(1,2,*('Raju',),**{'d':99})
