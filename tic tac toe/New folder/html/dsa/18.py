class account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_n = acc

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was debited")
        print("total balance =",self.get_balance())

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was credited")
        print("total balance =",self.get_balance())

    def get_balance(self):
        return self.balance



acc1 = account(49004,12345)
acc1.debit(1)
acc1.credit(6994)