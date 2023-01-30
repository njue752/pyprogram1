age=int(input("Enter your age:"))
country=input("Enter your country:")
countries=["kenya","tanzania","uganda"]
if age>=18 and country in countries:
    print("Eligible to vote")
else:
    print("Not eligible to vote")