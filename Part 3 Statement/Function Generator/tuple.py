#Tuple

def _tuple():
    result=0
    tuple1=(1,2,5,8,9)
    for i in tuple1:
        result=result+i
        print('result:',result,'i:',i)
        yield result

a1=_tuple()
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
