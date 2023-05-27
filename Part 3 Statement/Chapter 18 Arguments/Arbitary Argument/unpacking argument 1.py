#Unpacking argument

def f6(a,b,c,d):
    print(a,b,c,d)

f6(*(1,2,3,4))
f6(*(1,{'name':'Raju Mane','skill':['python','java']},'Rashi',4))
