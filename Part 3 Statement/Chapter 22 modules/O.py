#Using Import Method
'''
import M,N

add1=M.add(10,20)
print('From M:',add1)

sub1=M.sub(-7,-9)
print('From M:',sub1)

mul1=N.mul(3,-4)
print('From N:',mul1)

div1=N.div(3,2)
print('From N:',div1)

'''
#Using From Method
from M import add as Madd,sub as Msub
from N import mul as Nmul,div as Ndiv

add1=Madd(10,20)
print('Madd:',add1)

sub1=Msub(5,-4)
print('Msub:',sub1)

mul1=Nmul(-2,-8)
print('Nmul:',mul1)

div1=Ndiv(6,-4)
print('Ndiv:',div1)
