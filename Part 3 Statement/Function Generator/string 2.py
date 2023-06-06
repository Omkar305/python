#string

def string2():
    result=0
    s1='Omkar Savardekar'
    s2='python java'
    s3=''
    for i in s1:
        for j in s2:
            s3=i+j
            yield s3

a1=string2()
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
print(a1.__next__())
