#List Operation

list1=[]
list2=[5,8,3,6,4,8,9,5,4,2,7,1]
list3=['Bani','Mahika','Mitsu']
list4=[1,3,5,7,45.90,'Omkar','Dipti','Rashi',['HTML','CSS']]
list5=[1,58,43.89,(32,77,65),{'Name':'Chris','Age':25}]

print('list1',list1,len(list1))
print('list2',list2,len(list2))
print('list3',list3,len(list3))
print('list4',list4,len(list4))
print('list5',list5,len(list5))
print(80*'-')
print()

print('append')
list1.append(1)
print('list1.append(1)',list1,len(list1))

list2.append(19)
print('list2.append(19)',list2,len(list2))
print(80*'-')
print()

print('count')
a1=list2.count(4)
print('list2.count(4)',a1)

a2=list3.count('Bani')
print('list3.count("Bani")',a2)
print(80*'-')
print()

print('extend')
list1.extend([2,3,4,5,6,7,8,9,10])
print('list1',list1,len(list1))
print(80*'-')
print()

print('index')
a3=list2.index(5,3)
print('list2.index("5")',a3)

a4=list4.index('Omkar')
print('list4.index("Omkar")',a4)
print(80*'-')
print()

print('insert')
print('list2',list2,len(list2))
list2.insert(2,87.96)
print('list2',list2,len(list2))
print(80*'-')
print()

print('pop')
print('list2',list2,len(list2))
a5=list2.pop()
print('list2.pop()',a5,len(list2))














