#add tuple

def add_type(args):
    result=0
    for i in range(len(args)):
        for j in range(len(args[i])):
            result=result+args[i][j]
    return result
    

tuple1=(45,78,34)
tuple2=(56,90,89,67)
tuple3=(23,19,29)
def add_tuple(*pargs):
    print(pargs)
    result=add_type(pargs)
    print('addition of',type(pargs),result)
    

add_tuple(tuple1,tuple2,tuple3)

#add list

list1=[67,34,44,89]
list2=[87,50.32,11]
list3=[45,99,87,64]
def add_list(*pargs):
    list1=list(pargs)
    print('list1:',list1)
    result=add_type(pargs)
    print("addition of:",type(pargs),result)

add_list(list1,list2,list3)

#append multipe list

def append_list(*pargs):
    list1=list(pargs)
    print('list1:',list1)
    list2=[]
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            list2.append(list1[i][j])
    print('list2:',list2)

append_list(list1,list2,list3)











    














