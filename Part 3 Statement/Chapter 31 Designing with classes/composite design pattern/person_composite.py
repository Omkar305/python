class Person:
    def __init__(self,name,job=None,pay=0.0):
        self.name=name
        self.job=job
        self.pay=pay

    def giveRaise(self,percent):
        self.pay=int(self.pay+self.pay*percent)

    def lastName(self):
        return self.name.split()[-1]

    def __repr__(self):
        return '[Person: %s, %s, %s]'%(self.name,self.job,self.pay)

class Manager:
    def __init__(self,name,pay):
        self.person=Person(name,'MGR',pay)

    def giveRaise(self,percent,bonus):
        self.person.giveRaise(percent+bonus)

    def __getattr__(self,attr):
        return getattr(self.person,attr)

    def firstName(self):
        return self.name.split()[0]

    def middleName(self):
        return self.name.split()[1]

    def __repr__(self):
        return str(self.person)

omkar=Manager('Omkar Sunil Savardekar',50000)
print(omkar)

omkar.giveRaise(0.1,0.2)
print(omkar)

print(omkar.lastName())
print(omkar.firstName())
print(omkar.middleName())
