class FirstClass:
    def setdata(self,value):
        self.data=value

    def display(self):
        print(self.data)

x=FirstClass()
y=FirstClass()

x.setdata(10)
x.display()

y.setdata('Raju Mane')
y.display()

class SecondClass(FirstClass):
    def display(self):
        print('current value="%s"' %self.data)

z=SecondClass()
z.setdata(15.23)
z.display()

class ThirdClass(SecondClass):
    def __init__(self,value):
        self.data=value

    def __add__(self,other):
        return ThirdClass(self.data+other)

    def __str__(self):
        return '[ThirdClass:%s]' %self.data

    def mul(self,other):
        self.data=self.data*other

a=ThirdClass('Raju Mane')
a.display()
print(a)

b=a+'XYZ'
b.display()
print(b)

a.mul(3)
print(a)













