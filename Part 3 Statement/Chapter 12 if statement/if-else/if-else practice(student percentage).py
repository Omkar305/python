#student percentage

percent=int(input("Enter the student percentage:"))
if percent >= 80:
    print("First class")
else:
    print("Below First class")


percent=int(input("Enter the student percentage:"))
if percent >=60 and percent < 80:
    print("Second class")
else:
    print("Below Second class")


percent=int(input("Enter the student percentage:"))
if percent < 35:
    print("FAIL")
else:
    print("PASS")
