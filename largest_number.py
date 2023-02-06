#program to find the largest of three numbers
num1=int(input("Enter first value"))
num2=int(input("Enter second value"))
num3=int(input("Enter third value"))
if num1>num2 and num1>num3:
    print("num1 is the largest")
elif num2>num1 and num2>num3:
    print("num2 is the largest")
else:
    print("num3 is the largest")