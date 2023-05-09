#dict

dict1={}
print('dict1',dict1,len(dict1))

dict2={1,2,3,4,5,6,7,8,9,0}
print('dict2',dict2,len(dict2))

dict3={
    'name':'omkar',
    'age':23,
    'skill':['java','python','c','html','.net','c'],
    'laptop':{
        '2023':'Macbook Pro',
        '2022':'Macbook Air',
        '2021':'Alienware'
        }
    }
print('dict3',dict3,len(dict3))

dict4={'phno':(7486945690,6785678567)}
print('dict4',dict4,len(dict4))

a1=dict3.get('laptop')
print('a1',a1)

list1=dict3.items()
print('list1',list1,len(list1))

list4=list(dict3.items())
print('list4',list4,len(list4))

list2=list(dict3.keys())
print('list2',list2,len(list2))

list3=list(dict3.values())
print('list3',list3,len(list3))

a2=dict4.pop('phno')
print('a2',a2,len(a2))

a3=dict3.popitem()
print('a3',a3,len(a3))

a4=dict3.setdefault('laptop')
print('a4',a4)

dict3['laptop']={'2023':'Macbook pro',
                 '2022':'Macbook air',
                 '2021':'Dell'}
print('dict3',dict3,len(dict3))

print('indexing')
a5=dict3['laptop']['2022']
print('a5',a5,len(a5))

a6=dict3['skill'][-1]
print('a6',a6,len(a6))

print('slicing')
a7=dict3['skill'][-5:-1]
print('a7',a7,len(a7))


