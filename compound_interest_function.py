# Python program to find compound interest 
 
def compound_interest(principal, rate, time):
    Amount = principal * (pow((1 + rate / 100), time))
    C_interest = Amount - principal
    print("The compound interest is", C_interest)
 
compound_interest(25000, 5, 15)