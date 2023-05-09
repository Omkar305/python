#list comprehensions

list1=list(range(1,11))
print('list1:',list1,len(list1))

list2=[x+10 for x in list1]
print(list2)

list3=[x for x in list1 if x%2==0]
print('Even Number:',list3)

list4=[x for x in list1 if x%2==1]
print('Odd Number:',list4)
