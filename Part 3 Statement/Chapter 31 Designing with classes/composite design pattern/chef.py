class Employee:
    def __init__(self,name,etype=None,salary=0.0):
        self.name=name
        self.etype=etype
        self.salary=salary

    def giveRaise(self,percent):
        self.salary=self.salary+(self.salary*percent)

    def work(self):
        print(self.name,'does stuff')

    def __repr__(self):
        return 'employee -> name:%s,etype:%s,salary:%s' %(self.name,self.etype,self.salary)

class Chef(Employee):
    def __init__(self,name):
        chef_list=['PizzaChef','ChineseChef','ItalianChef']
        if self.__class__.__name__==chef_list[0]:
            Employee.__init__(self,name,self.__class__.__name__,25000)
        elif self.__class__.__name__==chef_list[1]:
            Employee.__init__(self,name,self.__class__.__name__,20000)
        elif self.__class__.__name__==chef_list[2]:
            Employee.__init__(self,name,self.__class__.__name__,30000)
        else:
            pass

def work(self):
    print(self.name,'makes food')

class PizzaChef(Chef):
    def __init__(self,name):
        Chef.__init__(self,name)

    def work(self):
        print(self.name,'makes pizza')

class ChineseChef(Chef):
    def __init__(self,name):
        Chef.__init__(self,name)

    def work(self):
        print(self.name,'makes chinese')

class ItalianChef(Chef):
    def __init__(self,name):
        Chef.__init__(self,name)

    def work(self):
        print(self.name,'makes italian')

class Server(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,self.__class__.__name__,10000)

    def work(self):
        print(self.name,'interfaces with customer')

if __name__=='__main__':

    chef_employee_list=[]

    raju=PizzaChef('Raju Mane')
    chef_employee_list.append(raju)

    omkar=ChineseChef('Omkar Savardekar')
    chef_employee_list.append(omkar)

    rashi=ItalianChef('Rashi Shelar')
    chef_employee_list.append(rashi)

    for obj in chef_employee_list:
        print(obj)
        obj.work()
        print()

    print()
    print()

    server_employee_list=[]

    makrand=Server('Makrand Salvi')
    server_employee_list.append(makrand)

    kuldeep=Server('Kuldeep Matal')
    server_employee_list.append(kuldeep)

    for obj in server_employee_list:
        print(obj)
        obj.work()
        print()














    














        






        
    

    











