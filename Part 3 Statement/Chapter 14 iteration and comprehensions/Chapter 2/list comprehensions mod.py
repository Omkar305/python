#modulus

list1=list([67,98,44,87,21,14,19,29,15,11])
print("list1:",list1,len(list1))

list2=[x%2 for x in list1]
print("list2:",list2)
print("list1:",list1)
