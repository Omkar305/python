hardness=int(input("Enter the Hardness:"))
carbon=float(input("Enter the carbon:"))
tensile=int(input("Enter the tensile:"))

if hardness>50 and carbon<1 and tensile>5600:
    print("grade 10")
elif hardness>50 and carbon<1:
    print("grade 9")
elif carbon<1 and tensile>5600:
    print("grade 8")
elif hardness>50 and tensile>5600:
    print("grade 7")
elif hardness>50 or carbon<1 or tensile>5600:
    print("grade 6")
else:
    print("grade 5")
