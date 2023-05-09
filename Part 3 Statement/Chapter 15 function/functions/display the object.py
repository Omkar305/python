#display the object

def display(obj):
    if isinstance(obj,str):
        for i in obj:
            print(i,end="")
    elif isinstance(obj,tuple):
        for i in obj:
            print(i)
    elif isinstance(obj,dict):
        for i in obj:
            print(i,obj[i])
    else:
        for i in obj:
            print(i)
            
            
list1=list(range(15))
list2=[1,23.45,67,'omkar',(57347,32644),{'name':'omkar','age':23}]
tuple1=(19,29,23,28)
string1='Everybody'
dict1={
    'name':'omkar',
    'age':23,
    'skill':['C','Java','Python']
    }

display(list1)
print()

display(list2)
print()

display(tuple1)
print()

display(string1)
print()
print()

display(dict1)
print()
