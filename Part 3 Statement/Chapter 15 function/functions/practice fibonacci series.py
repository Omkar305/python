#practice fibonacci series

def fib(num1,num2):
    print(num1)
    print(num2)
    res=0
    while res<=100:
        res=num1+num2
        print(res)
        num1=num2
        num2=res

fib(0,1)
