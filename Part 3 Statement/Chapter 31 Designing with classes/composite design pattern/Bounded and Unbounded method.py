class Maths:
    def add(self,a,b):
        return a+b

obj1=Maths()
x=obj1.add

#Bounded method are called by instance
print('by instance',obj1.add(10,20))
print('by method object',x(10,20))

#Unbounded method are called by class
print(Maths.add(obj1,50,50))

y=Maths.add
print(y(obj1,19,29))
