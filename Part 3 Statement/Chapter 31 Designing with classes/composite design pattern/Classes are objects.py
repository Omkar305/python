def factory(aclass,*pargs,**kargs):
    return aclass(*pargs,**kargs)

class Spam:
    def doit(self,message):
        print(message)

obj1=factory(Spam)      #Spam()
obj1.doit(10)
obj1.doit('Omkar Savardekar')

class Person:
    def __init__(self,name,job=None):
        self.name=name
        self.job=job

    def display(self):
        print(self.name,self.job)

x=factory(Person,'Omkar Savardekar','dev')
x.display()
        
