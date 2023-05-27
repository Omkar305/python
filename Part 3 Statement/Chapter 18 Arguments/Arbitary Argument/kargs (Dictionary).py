# **kargs(Dictionary)

def f4(**kargs):
    print(kargs)
    list1=list(kargs)
    for i in list1:
        print(i,kargs[i])

f4(name='Raju Mane',skill=['python','java'],phone=(7208122920,1234567890))
