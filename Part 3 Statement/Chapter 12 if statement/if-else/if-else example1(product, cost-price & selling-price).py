#product

cost_price=int(input("Enter the cost_price:"))
selling_price=int(input("Enter the selling_price:"))
if selling_price > cost_price:
    profit=selling_price - cost_price
    print("profit",profit)
else:
    loss=selling_price - cost_price
    print("loss",loss)
