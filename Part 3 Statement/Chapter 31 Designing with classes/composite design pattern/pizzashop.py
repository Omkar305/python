from chef import PizzaChef,Server

class Customer:
    def __init__(self,name):
        self.name=name

    def order(self,server):
        print(self.name,'order from',server)

    def pay(self,server):
        print(self.name,'pay for item to',server)

class Oven:
    def bake(self):
        print('oven bakes')

class PizzaShop:
    def __init__(self):
        self.server=Server('Makrand')
        self.chef=PizzaChef('Rashi')
        self.oven=Oven()

    def order(self,name):
        customer=Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

x=PizzaShop()
x.order('Dipti')




