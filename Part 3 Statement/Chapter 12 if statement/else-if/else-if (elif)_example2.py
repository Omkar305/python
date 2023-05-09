print("Qualifications")
print("1:Post-Graduate")
print("2:Graduate")
print()

print("Gender")
print("M:Male")
print("F:Female")
print()

gender=input("Enter the Gender:")
qualifications=int(input("Enter the Qualifications:"))
yrs=int(input("Enter the Years of Service:"))

if gender=='M' and qualifications==1 and yrs >= 10:
    salary=15000
    print("Salary:",salary)

elif gender=='M' and qualifications==2 and yrs >= 10:
    salary=10000
    print("Salary:",salary)

elif gender=='M' and qualifications==1 and yrs < 10:
    salary=10000
    print("Salary:",salary)

elif gender=='M' and qualifications==2 and yrs < 10:
    salary=7000
    print('Salary:',salary)

elif gender=='F' and qualifications==1 and yrs >= 10:
    salary=12000
    print("Salary:",salary)

elif gender=='F' and qualifications==2 and yrs >= 10:
    salary=9000
    print("Salary:",salary)

elif gender=='F' and qualifications==1 and yrs < 10:
    salary=10000
    print("Salary:",salary)

elif gender=='F' and qualifications==2 and yrs < 10:
    salary=6000
    print("Salary:",salary)

else:
    print("Please enter valid data")
