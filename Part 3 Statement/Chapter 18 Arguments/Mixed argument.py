#Mixed argument

def f1(a,b,c,d,e,f):
    print(a,b,c,d,e,f)

list1=[1,2,68.39,'omkar',(7685856762),{'company':'TCS'}]
tuple1=(6,89.6,'programming',(7636565965,8698328522))
dict1={
    'Name':'Omkar',
    'Age':23,
    'Phno':(8658659463),
    'Skill':['Java','Python','C']
    }
string1='Everybody in this country should learn programming'

f1(6,5,4,3,2,1)
f1(e=9,b=5,f=90,a=56,d=67,c=19)
f1(5,7,c=list1,d=87,e=dict1,f=78)
f1(a=tuple1,b=list1,c=dict1,d=string1,e='omkar',f=2*5*29/18+376-45)
print()


def f2(name,age,job,cmpname='TCS'):
    print('name:',name)
    print('age:',age)
    print('job:',job)
    print('cmpname:',cmpname)

f2('Omkar',23,'Developer','Google')
