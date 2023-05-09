per=int(input("Enter the Percentage:"))
if per >= 75:
    print("A")
else:
    if per >= 60:
        print("B")
    else:
        if per >= 40:
            print("C")
        else:
            print("FAIL")
            
