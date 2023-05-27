#list comprehension

a1=ord('o')
print('a1:',a1)

a2=ord('m')
print('a2:',a2)

a3=ord('k')
print('a3:',a3)

a4=ord('a')
print('a4:',a4)

a5=ord('r')
print('a5:',a5)

s1='python is everything for everyone'
list1=[]
for i in s1:
    list1.append(ord(i))
print('list1:',list1)

list2=[ord(i) for i in s1]
print('list2:',list2)

list3=[]
for i in range(25):
    list3.append(i)
print('list3:',list3)

list4=[i for i in range(20)]
print('list4:',list4)

list5=[pow(i,2) for i in range(1,26)]
print('list5:',list5)

list6=[i//4 for i in range(1,16) if i%2==1]
print('list6:',list6)

#nested

list7=[i+j for i in range(1,5) for j in range(1,5)]
print('list7:',list7)
print('-'*80)

list8=[(i,j) for i in range(1,11) if i%2==0 for j in range(1,11) if j%2==1]
print('list8:',list8)
print('-'*80)

list9=[i*j for i in range(1,8) for j in range(2,7)]
print('list9:',list9)
print('-'*80)

list10=[i+j for i in range(1,7) for j in range(1,11)]
print('list10:',list10)
print('-'*80)

list11=[i-j for i in range(-10,-12,-1) for j in range(5,8)]
print('list11:',list11)
print('-'*80)

list12=[i//j for i in range(15,10,-1) for j in range(2,5)]
print('list12:',list12)
print('-'*80)

list13=[(i,j)for i in range(2,15) if i%2==0 for j in range(8,23) if j%2==1]
print('list13:',list13)
print('-'*80)

list14=[i*j for i in range(1,11,2) for j in range(1,11)]
print('list14:',list14)
print('-'*80)






