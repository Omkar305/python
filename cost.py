def cal_discount(total,discount):
    cal_discount=total*discount/100
    total_price=total-cal_discount
    list1=[total_price,cal_discount]
    return list1

counter=0
while True:
    print()
    counter=counter+1
    print('customer',counter)
 
    def market_cal():
        num=float(input('product price:'))
        qty=int(input('enter the qty:'))
        total=0
        while(num != 0):
            total=total+num*qty
            print('total:',total)
            num=float(input('product price:'))
            qty=int(input('enter the qty:'))
            
        print('total product price:',total)
        
        if total>1000:
            list1=cal_discount(total,1)
            print('total_price:',list1[0],list1[1])
        elif total>2000:
            list1=cal_discount(total,2)
            print('total_price:',list1[0],list1[1])
        elif total>3000:
            list1=cal_discount(total,3)
            print('total_price:',list1[0],list1[1])
        elif total>4000:
            list1=cal_discount(total,4)
            print('total_price:',list1[0],list1[1])
        elif total>5000:
            list1=cal_discount(total,10)
            print('total_price:',list1[0],list1[1])
        else:
            print('total_price:',total,0.0)

    market_cal()


