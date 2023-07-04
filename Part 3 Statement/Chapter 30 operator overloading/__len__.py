class ShoppingCart:
    def __init__(self):
        self.items=[]

    def add_items(self,item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return repr(self.items)

cart=ShoppingCart()
print(len(cart))
cart.add_items('mobile')
cart.add_items('pen')
cart.add_items('book')
print(cart)
print(len(cart))
