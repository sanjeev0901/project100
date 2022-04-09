class atm(object):
    def __init__(self,cardHolderName,cardNumber, pin,cardExpiryDate):
        self.cardHolderName=cardHolderName
        self.cardNumber = cardNumber
        self.pin = pin
        self.cardExpiryDate = cardExpiryDate
        self.withdraw = 0
        self.deposit = 0
        self.transactions = 0
        self.transactionList = []
        self.balance = 0
        
    def withdrawFromACC(self):
        amount=int(input("Enter the amount you want to withdraw: "))
        if (amount) <= self.balance:
            print("Withdrawing...")
            self.balance -= (amount)
            print("Your balance is now: ", self.balance)
            self.transactions = self.transactions + 1
            self.transactionList.append("Withdraw: " + str(amount))
            print("Transaction successful!")
        else:
            print("Insufficient funds!")
        
                
    def depositToACC(self):
        amount=int(input("Enter the amount you want to deposit: "))
        print("Depositing...")
        self.balance += amount
        print("Your balance is now: ", self.balance)
        self.transactions = self.transactions + 1
        self.transactionList.append("Deposit: " + str(amount))
        print("Transaction successful!")
                            
    def balanceOfACC(self):
        print("Your balance is: ", self.balance)

    def transactionHistory(self):
        print("Transaction History: ")
        for i in range(0, self.transactions):
            print(self.transactionList[i])
        print("Your total transactions are: ", self.transactions)