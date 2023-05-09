tuple0=()
print('tuple0',tuple0,len(tuple0))

tuple1=(1,)
print('tuple1',tuple1,len(tuple1))

tuple2=(1,2,34.56,6,3,7,0,4)
print('tuple2',tuple2,len(tuple2))

tuple3=(
    1,
    20.93,
    'Suarez',
    {
        'season1':'summer',
        'season2':'monsoon',
        'season3':'spring',
        'season4':'winter',
        
        'fruits':
        {
            'summer':['Bananas','Bananas','Cherries'],
            'monsoon':['Pears','Apples','Jamun'],
            'spring':['Watermelon','Plum','Blackberry'],
            'winter':['Kiwis','Grapefruit','Oranges']
        }
    },
    (12,13,14,15),
    [83,37,90,239]
    )
print('tuple3',tuple3,len(tuple3))

tuple4=tuple3[-3]['season2']
print("tuple3['season2']",tuple4)

tuple5=tuple3[-3]['fruits']['monsoon'][-3]
print("tuple3[-3]['fruits']['monsoon'][-3]",tuple5)

tuple6=tuple3[-3]['fruits']['winter'][-1]
print("tuple3[-3]['fruits']['monsoon'][-3]",tuple6)

tuple7=tuple1+tuple2
print('tuple7',tuple7,len(tuple7))

tuple8=tuple2*2
print('tuple8',tuple8,len(tuple8))

tuple9=tuple2[-6:-2]
print('tuple9',tuple9,len(tuple9))

tuple10=tuple8.count(2)
print('tuple10',tuple10)

tuple11=tuple2.index(7)
print('tuple11',tuple11)


