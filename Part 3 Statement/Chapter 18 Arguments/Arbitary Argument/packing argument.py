#Packing argument/ also known as mixed argument

def f5(a,b,c,d,*pargs,**kargs):
    print(a,b,c,d,pargs,kargs)

f5(10,20,4,5,6,8,9,10,name='Raju Mane',skill=['python','java'])

