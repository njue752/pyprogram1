#program to output employee bonus
salary=int(input("Enter employee salary"))
service_years=float(input("Enter years of service"))
if (service_years>10):
    bonus=(salary*10/100)
    print("Bonus is",bonus)
elif(service_years>=6 and service_years<=10):
    bonus=(salary*8/100)
    print("Bonus is",bonus)
else:
    bonus=(salary*5/100)
    print("Bonus is",bonus)