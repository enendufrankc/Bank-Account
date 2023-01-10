import random
from datetime import datetime

class BasicAccount():
    acNum = 0
    def __init__(self, acName, openingBalance):
        self.name= acName
        self.balance = openingBalance
        BasicAccount.acNum += 1
        self.acNum = BasicAccount.acNum
        # self.cardNum = random(16)
        self.cardNum = self.generateCardNum()
        self.cardExp = self.generateCardExp()
        self.overdraft = False
        self.overdraft_limit = 0

    def generateCardNum(self) -> str:
        return ''.join([str(random.randint(0, 9)) for _ in range(16)])

    def generateCardExp(self) -> tuple:
        now = datetime.now()
        year = now.year
        year_yy = int(datetime(year, 1, 1).strftime('%y'))
        return now.month, year_yy + 3

    def deposit(self, amount: float):
        if amount <= 0:
            # raise ValueError(f'Invalid deposit £{amount}')
            print(f'Invalid deposit £{amount}')
        else:
            self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            # raise ValueError(f'Can not withdraw £{amount}')
            print(f'Can not withdraw £{amount}')
        else:
            self.balance -= amount
            print(f"{self.name} has withdrawn £{amount}", end=' ')
            print(f"balance is £{self.balance}", end='')
            # print(f"{self.name} has withdrawn £{amount}. New ballance is £{self.balance}", end='')

    def getAvailableBalance(self)  -> float:
        return self.balance
    
    def getBalance(self) -> float:
        return self.balance

    def printBalance(self):
        print(f'Balance: {self.balance}')

    def getName(self) -> str:
        return self.name

    def getAcNum(self) -> str:
        return str(self.acNum)

    def issueNewCard(self):
        self.cardNum = self.generateCardNum()
        self.cardExp = self.generateCardExp()

    def closeAccount(self) -> bool:
        if self.balance < 0:
            print(f'Can not close account due to customer being overdrawn by {-self.balance}')
            return False
        self.withdraw(self.balance)
        return True

    def __str__(self) -> str:
        return f'Name: {self.name}, Available balance: {self.getAvailableBalance()}, Overdraft: {self.overdraft}'


class PremiumAccount(BasicAccount):
    def __init__(self, name: str, balance: float, overdraftLimit: float):
        super().__init__(name, balance)
        self.overdraft = True
        self.overdraftLimit = overdraftLimit

    def withdraw(self, amount: float):
        if amount > self.balance + self.overdraftLimit:
            print(f'Can not withdraw £{amount}')
        else:
            self.balance -= amount
            print(f"{self.name} has withdrawn £{amount}", end=' ')
            print(f"balance is £{self.balance + self.overdraftLimit}", end='')

    def getAvailableBalance(self) -> float:
        return self.balance + self.overdraftLimit

    def getBalance(self) -> float:
        if self.balance < 0:
            return self.balance
        return self.balance

    def setOverdraftLimit(self, limit: float):
        self.overdraft = True
        self.overdraftLimit = limit

    def __str__(self) -> str:
        return f'Name: {self.name}, Available balance: {self.getAvailableAalance()}, Overdraft: {self.overdraft}, Overdraft limit: {self.overdraftLimit}'


ba = PremiumAccount("John Doe", 1000.00, 20000.00)
print(ba.getBalance())


