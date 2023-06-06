#List

def _list():
    result=0
    list1=[2,3,4,5,6]
    for i in list1:
        result=result+i
        print('result:',result,'i:',i)
        yield result

a1=_list()
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
