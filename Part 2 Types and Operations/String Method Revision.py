a1='  online Python compiler (interpreter) compiler to run Python online  '
a2='Omkar'
a3='OMKAR'
a4='Online Python Compiler'
a5='Omkar123'
a6='0123456789'
a7='_a1'
print(a1,len(a1))
print()

s1=a1.find('compiler')
print('find',s1)
print()
s2=a1.rfind('compiler')
print('rfind',s2)
print()
s3=a1.index('compiler')
print('index',s3)
print()
s4=a1.rindex('compiler')
print('rindex',s4)
print()
s5=a1.partition('(interpreter)')
print('partition',s5)
print()
s6=a1.rpartition('compiler')
print('rpartition',s6)
print()
s7=a1.split('Python')
print('split',s7)
print()
s8=a1.rsplit('to')
print('rsplit',s8)
print()
s9=a1.center(80,'#')
print('center',s9)
print()
s10=a1.ljust(80,'#')
print('ljust',s10)
print()
s11=a1.rjust(80,'#')
print('rjust',s11)
print()
s12=a1.strip()
print('strip',s12)
print()
s13=a1.rstrip()
print('rstrip',s13)
print()
s14=a2.join([' Do ' , ' Great ' , ' Work ' ])
print('join',s14)
print()
s15=a1.capitalize()
print('capitalize',s15)
print()
s16=a1.upper()
print('upper',s16)
print()
s17=a1.lower()
print('lower',s17)
print()
s18=a1.title()
print('title',s18)
print()
s19=a3.isupper()
print('isupper',s19)
print()
s20=a2.islower()
print('islower',s20)
print()
s21=a4.istitle()
print('istitle',s21)
print()
s22=a5.isalnum()
print('isalnum',s22)
print()
s23=a2.isalpha()
print('isalpha',s23)
print()
s24=a6.isdecimal()
print('isdecimal',s24)
print()
s25=a6.isdigit()
print('isdigit',s25)
print()
s26=a6.isnumeric()
print('isnumeric',s26)
print()
s27=a7.isidentifier()
print('isidentifier',s27)
print()
s28=a1.startswith('compiler',16,55)
print('startswith',s28)
print()
s29=a1.endswith(' ')
print('endswith',s29)
print()
s30=a1.count('Python',5,30)
print('count',s30)
s31=a4.replace('Python','Java')
print('replace',s31)
