list1=[]
print('list1',list1,len(list1))

list2=[11,21,31,41,51,61,71,81,91,101]
print('list2',list2,len(list2))

list3=['Breaking Bad','Suits','Peaky Blinders','Better Call Saul']
print('list3',list3,len(list3))

list4=[
    23,
    98.66,
    'Jordan',
    {
        'Manager':50000,
        'Developer':40000,
        'Tester':30000,
        'company':{
            '2023':'Apple',
            '2022':'Google',
            '2021':'Microsoft'
            }
    },
    (2375689267,8639404701)
    ]
print('list4',list4,len(list4))

print('concate')
a1=list2+list3
print('a1',a1,len(a1))

print('repetition')
a2=list2*2
print('a2',a2,len(a2))

print('indexing')
a3=list4[-2]['company']['2022']
print('a3',a3,len(a3))

a5=list4[-2]['company']['2023']
print('a5',a5,len(a5))

print('slicing')
a4=list3[-3:-1]
print('a4',a4,len(a4))

print('in place change')
list2[-2]=99
print('list2',list2,len(list2))

list4[-2]['Manager']=60000
print('list4',list4,len(list4))

list4[-2]['company']['2023']=['Deloitte']
print('list4',list4,len(list4))

list2.append(1)
print('list2',list2,len(list2))

a6=list2.count(21)
print('a6',a6)

list2.extend([1,2,3,7,9,4,9,0,3])
print('list2',list2,len(list2))

a7=list2.index(2)
print('a7',a7)

a8=list2.index(31)
print('a8',a8)

list2.insert(2,78)
print('list2',list2,len(list2))

a9=list2.pop()
print('a9',a9)

list2.remove(31)
print('list2',list2)

list2.reverse()
print('list2',list2)

list2.sort()
print('list2',list2)

list2.sort(reverse=True)
print('list2',list2)



