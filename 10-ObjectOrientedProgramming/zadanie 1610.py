class Konto:
    def __init__(self):
        self.balance=0

    def create_acc(self,nr):
        self.nr=nr

    def deposit(self,ile):
        self.balance+=ile

    def withdraw(self,ile):
        if ile <=self.balance:    
            self.balance-=ile
        else:
            print('non prendere')

    def display(self):
        print(f'Bank acc no: {self.nr}')
        print(f'Balance: PLN {self.balance}')


k=Konto()
k.create_acc('12 3456 5555 9090 1111 0000 7722')
k.display()
k.deposit(25.30)
k.display()
k.withdraw(31.70)
k.display()
k.withdraw(14)
k.display()
