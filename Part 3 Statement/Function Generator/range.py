#Range

def _range():
    result=0
    for i in range(10):
        result=result+i
        print('result:',result,'i:',i)
        yield result

a1=_range()
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())


