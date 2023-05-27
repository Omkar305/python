list1=[10,20,30,40,50,70]
def mylist(list1):
    if not list1:
        return 1
    else:
        return list1[0]+mylist(list1[1:])

result=mylist(list1)
print('result:',result)
    
