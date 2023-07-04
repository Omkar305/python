class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height

    def __eq__(self,other):
        if isinstance(self,Rectangle) and isinstance(other,Rectangle):
            return self.area()==other.area()
        else:
            return False

    def __ne__(self,other):
        if isinstance(self,Rectangle) and isinstance(other,Rectangle):
            return self.area()!=other.area()
        else:
            return False

    def __lt__(self,other):
        if isinstance(self,Rectangle) and isinstance(other,Rectangle):
            return self.area()<other.area()
        else:
            return False

    def __le__(self,other):
        if isinstance(self,Rectangle) and isinstance(other,Rectangle):
            return self.area()<=other.area()
        else:
            return False

    def __gt__(self,other):
        if isinstance(self,Rectangle) and isinstance(other,Rectangle):
            return self.area()>other.area()
        else:
            return False

    def __ge__(self,other):
        if isinstance(self,Rectangle) and isinstance(other,Rectangle):
            return self.area()>=other.area()
        else:
            return False

rect1=Rectangle(10,15)
print('rect1:',rect1.area())

rect2=Rectangle(5,9)
print('rect2:',rect2.area())

rect3=Rectangle(10,15)
print('rect3:',rect3.area())

rect4=Rectangle(15,20)
print('rect4:',rect4.area())

print('__eq__')
print(rect1==rect4)
print()
print('__ne__')
print(rect1!=rect2)
print()
print('__lt__')
print(rect1<rect4)
print()
print('__le__')
print(rect1<=rect4)
print()
print('__gt__')
print(rect1>rect4)
print()
print('__ge__')
print(rect1>=rect4)
print()








    

        
