class Employee:
    def __init__(self,name,job=None,pay=0.0):
        self.__name=name
        self.__job=job
        self.__pay=pay

    def __giveRaise(self,percent):
        self.__pay=int(self.__pay+self.__pay*percent)

x=Employee('Rashi Shelar','Dev',35000)
print(x._Employee__name)
print(x._Employee__job)
print(x._Employee__pay)

x._Employee__giveRaise(0.10)
print(x._Employee__pay)
