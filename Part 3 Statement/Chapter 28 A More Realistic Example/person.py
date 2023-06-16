class AttrDisplay:
    def gatherAttrs(self):
        attrs=[]
        for key in sorted(self.__dict__):
            attrs.append('%s=%s'%(key,getattr(self,key)))
        return ','.join(attrs)

    def __repr__(self):
        return '[%s:%s]'%(self.__class__.__name__,self.gatherAttrs())

class Person(AttrDisplay):
    def __init__(self,name,mobileno,add=None,job=None,pay=0.0):
        self.name=name
        self.mobileno=mobileno
        self.add=add
        self.job=job
        self.pay=pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self,percent):
        self.pay=int(self.pay*(1+percent))

class Manager(Person):
    def __init__(self,name,mobileno,add,pay):
        Person.__init__(self,name,mobileno,add,'MGR',pay)
 
    def giveRaise(self,percent,bonus=0.2):
        Person.giveRaise(self,percent+bonus)

    def firstName(self):
        return self.name.split()[-2]
    

if __name__=='__main__':
    raju=Person(name='Raju Mane',mobileno=9833395327,job='dev',pay=25000)
    omkar=Person(name='Omkar Savardekar',mobileno=8956238920,job='jr.dev',pay=15000)
    makrand=Person(name='Makrand Salvi',mobileno=9996669990)
    print()
    print(raju.name,raju.job,raju.pay)
    print(omkar.name,omkar.job,omkar.pay)
    print(makrand.name,makrand.job,makrand.pay)
    print()
    print(raju.name.split()[-1])
    print(omkar.name.split()[-1])
    print(makrand.name.split()[-1])
    print()
    print(raju.lastName())
    print(omkar.lastName())
    print(makrand.lastName())
    print()
    raju.giveRaise(0.1)
    print(raju.pay)
    omkar.giveRaise(0.05)
    print(omkar.pay)
    makrand.giveRaise(0.0002)
    print(makrand.pay)
    print()
    print(raju)
    print(omkar)
    print(makrand)
    print()
    rashi=Manager('Rashi Shelar',9874563210,'MGR',50000)
    print(rashi)
    rashi.giveRaise(0.1)
    print(rashi)
    print(rashi.firstName())
    
    
