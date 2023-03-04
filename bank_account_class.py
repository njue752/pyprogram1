#class with methods to compute customer details

class Bank_Account:
    def _init_(self):
        self.balance=0
        
    def customer_details(self):
        name='Martin Nthiga'
        print("Hello,welcome",name)
        acc_no=1169176923
        print("Your account number is : ",acc_no)
        date_of_opening=(input("Enter date of account opening: "))
        print("Date of account opening is:",date_of_opening)
        self.balance=0
        print("Your current balance: ", self.balance,"\n")
        
    def deposit(self):
        amount=int(input("Enter amount to be deposited into your account:"))
        self.balance=+amount
        print("Amount deposited into the account :", amount)
    def withdraw(self):
        amount=int(input("Enter amount to withdraw: "))
        if (self.balance>=amount):
            self.balance-=amount
            print("You withdrew:", amount)
        else:
            print("Insufficient balance ")
    def check_balance(self):
        print("Current balance is:", self.balance)
     
Bal=Bank_Account()

Bal.customer_details()
Bal.deposit()
Bal.withdraw()
Bal.check_balance()

            

