a1='Fifth generation Computers Devices are based on AI.'
a2='Fifth123'
a3='First'
a4='012456789'
a5='_a'
a6='First generation,Second generation,Third generation'



s1=a1.capitalize()
print('capitalize',s1)
s2=a1.upper()
print('upper',s2)
s3=a1.lower()
print('lower',s3)
s4=a1.title()
print('title',s4)
s5=a1.center(60,'*')
print('center',s5)
s6=s2.isupper()
print('isupper',s6)
s7=s3.islower()
print('islower',s7)
s8=a2.isalnum()
print('isalnum',s8)
s9=a3.isalpha()
print('isalpha',s9)
s10=a4.isdecimal()
print('isdecimal',s10)
s11=a4.isdigit()
print('isdigit',s11)
s12=a4.isnumeric()
print('isnumeric',s12)
s13=a5.isidentifier()
print('isidentifier',s13)
s14=a6.count('generation',10,35)
print('count',s14)
s15=a6.index('generation',30,60)
print('index',s15)
s16=a6.find('Second',10,50)
print('find',s16)
s17=a1.startswith('Fifth',0,10)
print('startswith',s17)
s18=a1.endswith('based',-11,-1)
print('endswith',s18)














