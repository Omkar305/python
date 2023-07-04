class Printable:
    def print_info(self):
        print('Employee name',self.name)
        print('Employee id',self.employee_id)

class Loggable:
    def log_action(self,action):
        print('loggable action',action)

    def print_info(self):
        print('Employee name',self.name)
        print('Employee id',self.employee_id)
        print('you are manager')

class Employee(Printable,Loggable):
    def __init__(self,name,employee_id):
        self.name=name
        self.employee_id=employee_id

class Manager(Employee):
    def __init__(self,name,employee_id,dept):
        Employee.__init__(self,name,employee_id)
        self.dept=dept

manager=Manager('Dipti Shah',124578,'HR')

manager.print_info()
print()
Loggable.print_info(manager)
print()
manager.log_action('Create manager')











