#dict

dict1={}
print('dict1',dict1,len(dict1))

dict2={'name':'Omkar',
       'age':23,
       'skill':['photoshop','msi','programming'],
       'phone':(1234567890,8888888888)
       }
print('dict2',dict2,len(dict2))

dict3={'2022':'juventus',
       '2021':'barcelona',
       '2020':'madrid'
       }
print('dict3',dict3,len(dict3))
print(60*'-')
print()

a1=dict2['name']
print('a1',a1)

a2=dict2['skill']
print('a2',a2)

a3=dict2['skill'][-2]
print('a3',a3)

a4=dict2['phone']
print('a4',a4)

a5=dict2['phone'][0]
print('a5',a5)

dict1['Top-G']='Andrew tatte'
print('dict1',dict1,len(dict1))

dict3['2019']='arsenal'
print('dict3',dict3,len(dict3))

dict3['2019']='manchester united'
print('dict3',dict3,len(dict3))

del dict3['2020']
print('dict3',dict3,len(dict3))

dict3['2020']='madrid'
print('dict3',dict3,len(dict3))

dict3['2019']='paris'
print('dict3',dict3,len(dict3))

dict2['skill']=['photoshop','programming']
print('dict2',dict2,len(dict2))

dict2['skill'][0]='googler'
print('dict2',dict2,len(dict2))
print()

dict3['2018']='alnasir'
dict3['2017']='chelsea'
print('dict3',dict3,len(dict3))

list1=list(dict3.items())
print("")





















