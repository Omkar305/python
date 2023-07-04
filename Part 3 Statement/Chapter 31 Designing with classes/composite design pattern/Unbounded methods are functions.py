class Selfless:
    def __init__(self,data):
        self.data=data

    def selfless(arg1,arg2):
        return arg1+arg2

    def normal(self,arg1,arg2):
        return self.data+arg1+arg2

x=Selfless(10)
print(x.data)

print(x.normal(10,20))

print(Selfless.selfless(50,50))
