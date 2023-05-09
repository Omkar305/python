#dict

dict1={
    'Name':'Omkar',
    'Age':23,
    'Skill':['Java','Python'],
    'Phone No':(6868923556,6786542598)
    }
print('dict1',dict1,len(dict1))

i1=iter(dict1)
print(i1)
a1=i1.__next__()
print(a1,dict1[a1])
a2=i1.__next__()
print(a2,dict1[a2])
a3=i1.__next__()
print(a3,dict1[a3])
a4=i1.__next__()
print(a4,dict1[a4])
a5=i1.__next__()
print(a5,dict[a5])
