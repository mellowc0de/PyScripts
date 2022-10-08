class BankAccount:
    def __init__(self, accountHolder):
        self._balance = 0
        self._name = accountHolder
        with open(self._name + 'Ledger.txt', 'w') as ledgerFile:
            ledgerFile.write('Balance is 0\n')
    
    def deposit(self, amount):
        if amount <= 0:
            return 'Negative Deposits not allowed'
        self._balance += amount
        with open(self._name + 'Ledger.txt', 'a') as ledgerFile:
            ledgerFile.write('Deposit ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self._balance) + '\n')
    
    def withdraw(self, amount):
        if self._balance < amount or amount < 0:
            return 'Not enough in account, or withdraw is negative'
        self._balance -= amount
        with open(self._name + 'Ledger.txt', 'a') as ledgerFile:
            ledgerFile.write('Withdraw ' + str(amount) + '\n')
            ledgerFile.write('Balance is ' + str(self._balance) + '\n')


acct = BankAccount('Alice')
acct.deposit(120)
acct.withdraw(400)

# Changing _name or _balance is impolite but allowed
acct._balance = 1000000000
acct.withdraw(1000)

acct._name = 'Bob'
acct.withdraw(1000)