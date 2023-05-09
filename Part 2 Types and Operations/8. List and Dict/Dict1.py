#dict1

dict1={'name':'Omkar',
       'age':23,
       'phone':(6866698229,9693763573,6785693579),
       'skills':['python','.net','mysql'],
       'yrs':{'2023':'F.Y.Bsc',
              '2024':'S.Y.Bsc',
              '2025':['Degree','M.Sc']
              }
       }
print('dict1',dict1,len(dict1))

dict2=dict1['skills'][-2]
print('dict2',dict2)

dict3=dict1['yrs']['2025'][-1]
print('dict3',dict3)

dict4=dict1['phone'][-2]
print('dict4',dict4)
