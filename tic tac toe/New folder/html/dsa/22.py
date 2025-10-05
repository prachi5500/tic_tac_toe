class account:
    
    def __init__(self, bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance-= amount
        
        print("rs.",amount,"was debited")    
        print("total amount=",self.get_balance())
    def credit(self,amount):
        self.balance+= amount
        print("rs.",amount,"was credited")    
        print("total amount=",self.get_balance())
    def get_balance(self):
        return self.balance
    
acc1= account (10000,12345)
acc1.credit(5000)
acc1.credit(300)
acc1.debit(1000)

# s2=student()
# print(s2.name)

#  
