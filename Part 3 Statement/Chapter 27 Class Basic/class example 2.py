class rec:
    pass

rec.name='Raju Mane'
rec.age=32
print(rec.name,rec.age)

x=rec()
y=rec()
print('x',x.name,x.age)
print('y',y.name,y.age)

x.name='Rashi Shelar'
y.name='Omkar Savardekar'
print(rec.name,x.name,y.name)
