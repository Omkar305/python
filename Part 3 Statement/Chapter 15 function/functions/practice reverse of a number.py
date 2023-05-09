#practice reverse of a number


def rev(num):
    rev=0
    while num!=0:
        remainder=num%10
        rev=rev*10+remainder
        num=num//10
    print("Reverse of a number is:",rev)

rev(1234)
rev(89)
rev(67654785)
