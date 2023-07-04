class SharedData:
    data=100
    def __init__(self,data1,data2):
        self.data1=data1
        self.data2=data2

    def add(self):
        c=self.data1+self.data2
        return c

    def __repr__(self):
        return '[SharedData=%s,%s]'%(self.data1,self.data2)

x=SharedData(10,20)
print(x.data1,x.data2)
print(x)
a1=x.add()
print('a1:',a1)
print('SharedData:data using x instance',x.data)
print()

y=SharedData(30,40)
print(y)
a2=y.add()
print('a2:',a2)
print('SharedData:data using y instance',y.data)
print()

print('SharedData:data',SharedData.data)

SharedData.data=50
print('SharedData:data',SharedData.data)
print('SharedData:data using x instance',x.data)
print('SharedData:data using y instance',y.data)

x.data=20
print('SharedData:data',SharedData.data)
print('SharedData:data using x instance',x.data)
print('SharedData:data using y instance',y.data)



