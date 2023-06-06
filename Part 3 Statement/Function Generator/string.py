#String

def _string():
    result=''
    string1='Omkar'
    for i in string1:
        result=result+i
        print('result:',result,'i:',i)
        yield result

a1=_string()
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
print(a1.__next__())
