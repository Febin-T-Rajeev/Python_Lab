class Bankaccount:
    def __init__(self):
        self.accno=210041
        self.name="Shigin"
        self.acctype="savings"
        self.balance=0
    def deposit(self):
        amount=int(input("enter the amount to deposit:\t"))
        self.balance+=amount
        print("Amount succsfully deposited")
    def withdraw(self):
        amount=int(input("enter the amount to withdraw:\t"))
        if self.balance>=amount:
            self.balance-=amount
            print("succesfully withdrawn")
        else:
            print("insufficient balance")
    def display(self):
        print("Account number=",self.accno,"\nName=",self.name,"\nAccount type=",self.acctype,"\nAvailable balance=",self.balance)
ob=Bankaccount()
ob.deposit()
ob.withdraw()
ob.display()
