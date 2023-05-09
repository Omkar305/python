tuple1=()
print('tuple1',tuple1,len(tuple1))

tuple2=(1,2,3,4,5)
print('tuple2',tuple2,len(tuple2))

tuple3=(
    1,23.45,
    'Omkar Savardekar',
    {
        'name':'Omkar Savardekar',
        'skill':['python','java','c']
        },
    (1,2,3,10.23),
    [1,4,61.50,61.90]
    )
print('tuple3',tuple3,len(tuple3))

tuple4=(8,7,9,5,1,2,3)
print('tuple4',tuple4,len(tuple4))
print(80*'-')
print()

print('indexing')
a1=tuple2[-3]
print('a1',a1)

a2=tuple3[-3]['skill'][-2]
print('a2',a2)
print(80*'-')
print()

print('slicing')
a3=tuple4[1:4]
print('a3',a3)

a4=tuple3[-3:-1]
print('a4',a4)
print(80*'-')
print()

print('concate')
tuple5=tuple3+tuple4
print('tuple5',tuple5,len(tuple5))

tuple6=tuple2+tuple4
print('tuple6',tuple6,len(tuple6))
print(80*'-')
print()

print('repeat')
tuple7=tuple2*2
print('tuple7',tuple7,len(tuple7))

tuple8=tuple4*3
print('tuple8',tuple8,len(tuple8))
print(80*'-')
print()

print('count')
a5=tuple8.count(5)
print('tuple8.count(5)',a5)

a6=tuple8.count(0)
print('tuple8.count(0)',a6)
print(80*'-')
print()

print('index')
a7=tuple8.index(5)
print('tuple8.index(5)',a7)

a8=tuple8.index(0)
print('tuple8.index(0)',a8)






































































