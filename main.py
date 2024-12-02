class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.acco_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("total = ", self.bal())
    def credit(self,amount):
        self.balance += amount
        print("Rs", amount, "is credited")
        print("total = ", self.bal())

    def bal(self):
        return self.balance

acc1 = Account(1000, 2906)
acc1.debit(100)
acc1.credit(10000352353532)
