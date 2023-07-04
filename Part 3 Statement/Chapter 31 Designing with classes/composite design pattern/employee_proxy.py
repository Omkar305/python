class Employee:
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary

    def __repr__(self):
        return '[Employee: %s, %s, %s]'%(self.name,self.position,self.salary)

class Employee_proxy:
    def __init__(self,target):
        self.target=target

    def __getattr__(self,attr):
        return getattr(self.target,attr)

    def getName(self):
        print(self.name)

    def getPosition(self):
        print(self.position)

    def getSalary(self):
        if self.position=='mgr':
            print(self.salary)
        else:
            raise PermissionError("Access to salary information is restricted")

raju=Employee('Raju Mane','dev',25000)
print(raju)
raju_proxy=Employee_proxy(raju)
raju_proxy.getName()
raju_proxy.getPosition()
print()

dipti=Employee('Dipti Shah','mgr',50000)
print(dipti)
dipti_proxy=Employee_proxy(dipti)
dipti_proxy.getName()
dipti_proxy.getPosition()
dipti_proxy.getSalary()
