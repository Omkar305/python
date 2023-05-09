#even-odd

def even_odd():
    i=1
    while i<=10:
        num=int(input("Enter the number:"))
        if num%2==0:
            print("Even number",num)
        else:
            print("Odd number",num)
        i=i+1

even_odd()
