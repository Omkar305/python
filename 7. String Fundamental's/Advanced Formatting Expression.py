x=8055
print('x:',x)
res='integer:...%d...%-10d...%015d...%+10d' %(x,x,x,x)
print(res)

x1=1.23456789
print('x1:',x1)
res='%e | %f | %g' %(x1,x1,x1)
print(res)

x2=1.4e-10
print('x2:',x2)
res='%e | %f | %g' %(x2,x2,x2)
print(res)

x3=1.735633
res='%15.5f | %15.2f | %15.2f' %(x3,x3,x3)
print(res)

d1={
    'Name':'Omkar',
    'Age':23,
    'Edu':'B.Sc',
    'Avg':66.6042
    }
print(d1)
res='%(Name)s....%(Age)d....%(Edu)s....%(Avg)f' %d1
print(res)
