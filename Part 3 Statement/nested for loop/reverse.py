#example 1

num=int(input("Enter the number:"))
for i in range(num,0,-1):
    for j in range(i):
        print(j,end='')
    print()
