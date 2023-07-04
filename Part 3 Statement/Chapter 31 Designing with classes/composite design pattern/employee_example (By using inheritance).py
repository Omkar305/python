class Employee:
    list1=[x for x in range(10)]
    def __init__(self,name,job=None,pay=0.0):
        self.name=name
        self.job=job
        self.pay=pay

    def lastName(self):
        return self.name.split()[-1]

    def add(self,a,b):
        return a+b

    def __repr__(self):
        return '[Employee: %s, %s, %s]'%(self.name,self.job,self.pay)

class Manager(Employee):
    def __init__(self,name,pay):
        Employee.__init__(self,name,'MGR',pay)

    def firstName(self):
        return self.name.split()[0]

    def middleName(self):
        return self.name.split()[1]

raju=Employee('Raju Mane','dev',25000)
print(raju)

omkar=Employee('Omkar Savardekar','dev',25000)
print(omkar)

print(omkar.add(10,20))
print(Employee.add(omkar,10,20))

dipti=Manager('Dipti Shah',50000)
print(dipti)
