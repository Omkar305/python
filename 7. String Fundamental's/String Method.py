#string method
a1='Identifiers are Name that are Given to varios Program elements.'
a2='generation Of computer,generation Of laptop,generation of AI'
a3='GENERATION'
a4='generation'
a5='generation123'
a6='First'
a7='0123456789'

s1=a1.capitalize()
print(s1)
s2=a1.upper()
print(s2)
s3=a1.lower()
print(s3)
s4=a1.title()
print(s4)
s5=a1.center(75,'*')
print(s5)
s6=a3.isupper()
print(s6)
s7=a4.islower()
print(s7)
s8=a5.isalnum()
print(s8)
s9=a6.isalpha()
print(s9)
s10=a7.isnumeric()
print(s10)
s11=a7.isdecimal()
print(s11)
s12=a7.isdigit()
print(s12)
s13=a2.index('Of',1,15)
print(s13)
s14=a2.startswith('generation')
print(s14)
s15=a2.endswith('AI')
print(s15)
s16=a2.replace('generation','year')
print(s16)
s17=a1.count('are',15)
print(s17)
