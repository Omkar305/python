#practice prime numbers

num=int(input("Enter the number:"))
counter=0
i=1
if num==0 or num==1:
    print("number 0 and 1 are not prime number")
else:
    while i<=num:
        if num%i==0:
            counter=counter+1
        i=i+1

if counter==2:
    print("Prime Number")
else:
    print("Not prime number")
            
    
