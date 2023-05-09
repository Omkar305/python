#Marks of Students

total_students=int(input("Enter the total no of students: "))
student_no=1
while student_no <= total_students:
    print("Student No: ",student_no)
    name=input("Enter the name: ")
    cls=input("Enter the class: ")
    m1=int(input("Enter the Marks1: "))
    m2=int(input("Enter the Marks2: "))
    m3=int(input("Enter the Marks3: "))
    m4=int(input("Enter the Marks4: "))
    m5=int(input("Enter the Marks5: "))
    total=m1+m2+m3+m4+m5
    print("Total marks: ",total)
    per=total/500*100
    print("Percentage: ",per)

    if per>=75:
        print("A")
    elif per>60:
        print("B")
    elif per>50:
        print("C")
    elif per>35:
        print("D")
    else:
        print("Fail")
    student_no=student_no+1
