#list

list1=[1,
       30.50,
       ['python','java'],
       {'name':'omkar',
        'phone':3972470021,
        'skills':['python','c++','java','mysql','.net']},
       (85,55,20,10,{'2022':'GT','2021':'MI','2018':['MI','CSK']})
       ]
print('list1',list1,len(list1))

list2=list1[-2]
print('list2',list2)

list3=list1[3]['skills'][-3]
print('list3',list3)

list4=list1[-1][2]
print('list4',list4)

list5=list1[-1][-1]['2021']
print('list5',list5)

list6=list1[-1][-1]['2018'][-1]
print('list6',list6)

list7=[1,2,3,4,5,6,7,8,9,10]
print('list7',list7,len(list7))

list8=list7[-5:-2]
print('list8',list8)

list9=list7[-6:]
print('list9',list9)

list10=list7[:-4]
print('list10',list10)

list11=list7[2:]
print('list11',list11)

list12=list7[:]
print('list12',list12)



