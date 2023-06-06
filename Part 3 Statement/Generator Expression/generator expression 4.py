num=int(input("Enter the number:"))
def f1(name,value):
    for i in range(value):
        print(name.__next__())

list1=(x*y for x in range(1,11) for y in range(1,11))
f1(list1,100)
print()

list2=(x+y for x in range(1,5) for y in range(6,8))
f1(list2,8)
print()

list3=(x for x in range(num))
f1(list3,num)
