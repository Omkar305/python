#salary

basic_salary=int(input("Enter the basic_salary:"))
if basic_salary < 1500:
    HRA=basic_salary*(10/100)
    DA=basic_salary*(90/100)
    total=basic_salary + HRA + DA
    print("Total salary:",total)
else:
    HRA=500
    DA=basic_salary*(98/100)
    total=basic_salary + HRA + DA
    print("Total salary:",total)


