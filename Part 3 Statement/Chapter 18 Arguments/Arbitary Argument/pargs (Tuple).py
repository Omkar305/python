# *pargs(Tuples)

def f3(*pargs):
    print(pargs)
    for i in pargs:
        print(i)

f3(1)
f3(1,2,3,4)
f3(1,2,[1,5,6],'Raju',{'name':'raju','skill':['python','java']})
