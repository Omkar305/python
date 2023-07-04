class AttrDisplay:
    def gatherAttrs(self):
        attrs=[]
        for key in self.__dict__:
            attrs.append('%s=%s'%(key,getattr(self,key)))
        return ','.join(attrs)

    def __repr__(self):
        return '[%s:%s]'%(self.__class__.__name__,self.gatherAttrs())

class Employee(AttrDisplay):
    def __init__(self,name,job,pay,dept,mobile=0.0,address=''):
        self.name=name
        self.job=job
        self.pay=pay
        self.dept=dept
        self.mobile=mobile
        self.address=address

    def giveRaise(self,percent):
        if self.pay==0.0:
            pass
        else:
            self.pay=int(self.pay*(1+percent))

class Manager(Employee):
    def __init__(self,name,pay,dept):
        Employee.__init__(self,name,'MGR',pay,dept)

    def giveRaise(self,percent,bonus):
        if self.dept=='IT':
            Employee.giveRaise(self,percent+bonus)
        elif self.dept=='Finance':
            Employee.giveRaise(self,percent+bonus)
        elif self.dept=='Admin':
            Employee.giveRaise(self,percent+bonus)
        else:
            pass

if __name__=='__main__':
    raju=Employee('Raju Mane','dev',15000,'IT')
    print(raju)
    raju.giveRaise(0.2)
    print(raju)
    print()

    aryan=Employee('Aryan Parle','',0.0,'Finanace')
    print(aryan)
    aryan.giveRaise(0.1)
    print(aryan)
    print()

    makrand=Employee('Makrand Salvi','Sys Admin',10000,'Admin')
    print(makrand)
    makrand.giveRaise(0.2)
    print(makrand)
    print()

    dipti=Manager('Dipti Shah',25000,'IT')
    print(dipti)
    dipti.giveRaise(0.2,0.4)
    print(dipti)
    print()

    rashi=Manager('Rashi Shelar',30000,'Finance')
    print(rashi)
    rashi.giveRaise(0.3,0.6)
    print(rashi)
    print()

    omkar=Manager('Omkar Savardekar',35000,'Admin')
    print(omkar)
    omkar.giveRaise(0.4,0.7)
    print(omkar)

    
    
