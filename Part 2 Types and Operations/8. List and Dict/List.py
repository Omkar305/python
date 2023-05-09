l1=[]
print('l1',l1,len(l1))

l2=[1,2,3,4,5,6,7,8,9,10]
print('l2',l2,len(l2))

l3=['Omkar',12,83.894,['Apple','Google','Microsoft']]
print('l3',l3,len(l3))

l4=[
    'Devishi',
    49,
    76.96,
    {'Name':'Delraz','Age':28,'Skill':['Java','Python']},
    (2,7,6,83.93)
    ]
print('l4',l4,len(l4))
print()

print('concate')
l5=l2+l3
print('l5',l5,len(l5))

l6=l2+l3+l4
print('l6',l6,len(l6))
print()

print('Repetition')
l7=l3*10
print('l7',l7,len(l7))
print()

print('indexing')
l8=l3[3]
print('l8',l8)

l9=l3[3][1]
print('l9',l9)

l10=l3[-1][-3]
print('l10',l10)

print('l6',l6,len(l6))
l11=l6[-2]['Skill'][1]
print('l11',l11)
print()

print('slicing')
print('l4',l4)
l12=l4[1:4]
print('l12',l12,len(l12))

l13=l6[-9:-1]
print('l13',l13,len(l13))

m1=[
    [11,97,45],
    [45,86,37],
    [84,64,99]
    ]
print('m1',m1,len(m1))

m2=m1[1][2]
print('m2',m2)

m3=m1[-3][-1]
print('m3',m3)
print()

print('In place change')
print('l4',l4,len(l4))

l4[-5]='Rhea'
print('l4',l4)

l4[-2]['Name']='Maya'
print('l4',l4)


print('l2',l2)
l2[3:7]=[50,60,70.45,80]
print('l2',l2)

l2[1:1]=[99]
print('l2',l2)

l2[3:7]=[]
print('l2',l2)

l2[1:3]=[88,39,46,99,70]
print('l2',l2)





























































