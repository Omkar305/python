def fetch(obj,index):
    return obj[index]

s1='Omkar'
list1=[1,2,3,78,45,99]
tuple1=(1,2,3,19,29,54,35)

def f1(obj,index):
    try:
        result=fetch(obj,index)
        print(result)
    except Exception as e:
        print(e)

f1(s1,5)
f1(list1,6)
f1(tuple1,7)
