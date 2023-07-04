class Employee:
    def __init__(self,name,job=None,pay=0.0):
        self.name=name
        self.job=job
        self.pay=pay

    def __repr__(self):
        return '[Employee:%s, %s, %s]'%(self.name,self.job,self.pay)

    def __del__(self):
        print('Goodbye:',self.name)

omkar=Employee('Omkar Savardekar','CEO',30000)
print(omkar)
omkar=10
print(omkar)
omkar=20
print(omkar)

        
