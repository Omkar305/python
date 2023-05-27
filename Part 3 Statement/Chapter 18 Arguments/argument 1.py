#By positional

#Inmutable
b=98
def f1(a):
    a=65
    print(a)

f1(b)
print(b)


#Mutable
l1=['Omkar',29]
x=19

def f2(a,b):
    b[-2]='Makrand'
    b[-1]=99
    print(b)
    print(a)

f2(x,l1[:])
print(l1)
print(x)
