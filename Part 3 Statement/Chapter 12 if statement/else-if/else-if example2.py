print("Qualifications")
print("1:Post-Graduate")
print("2:Graduate")
print()
print("Gender")
print("M:Male")
print("F:Female")
print()

gender=input("Enter the gender:")
qualifications=int(input("Enter the Qualifications"))
yrs=int(input("Enter the Years of Service:"))

if gender=='M' and qualifications==1 and yrs>=10:
    salary=15000
    print("salary",salary)
elif gender=='M' and qualifications==2 and yrs>10:
    salary=10000
    print("salary",salry)
elif gender=='M' and qualifications==1 and yrs<10:
    salary=10000
    print("salary",salary)
elif gender=='M' and qualifications==2 and yrs<10:
    salary=7000
    print("salary",salary)
elif gender=='F' and qualifications==1 and yrs>=10:
    salary=12000
    print("salary",salary)
elif gender=='F' and qualifications==2 and yrs>=10:
    salary=9000
    print("salary",salary)
elif gender=='F' and qualifications==1 and yrs<10:
    salary=10000
    print("salary",salary)
elif gender=='F' and qualifications==2 and yrs<10:
    salary=6000
    print("salary",salary)
else:
    print("please enter valid data")






















