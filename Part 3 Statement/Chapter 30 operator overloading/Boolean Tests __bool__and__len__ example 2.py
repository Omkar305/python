class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height

    def __bool__(self):
        return self.width>0 and self.height>0

rect1=Rectangle(10,20)
rect2=Rectangle(10,0)

def text_bool(obj):
    if obj:
        print('obj:',obj.area())
    else:
        print('width or height should be greater than zero')

text_bool(rect1)
text_bool(rect2)
