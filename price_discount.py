amount_purchased=float(input("Enter the amount purchased"))
if amount_purchased>1000:
    discount=0.05*amount_purchased
    print("The discount is:",discount)
else:
    print("No discount is given")
                       