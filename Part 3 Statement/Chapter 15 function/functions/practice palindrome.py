#practice palindrome

def pal(num):
    temp=num
    rev=0
    while num!=0:
        remainder=num%10
        rev=rev*10+remainder
        num=num//10
    print("Reverse of the number is:",rev)

    if temp==rev:
        print("The number is Palindrome")
    else:
        print("The number is not palindrome")

num=int(input("Enter the number:"))
pal(num)
