import ATM

print("Welcome to the ATM!")
print("Please enter your card details----------------------------------------------------")
name=input("Enter your card name: ")
cardNumber=input("Enter your card number: ")
pin=input("Enter your pin: ")
expiryDate=input("Enter your card ExpiryDate: ")
print("Thank you!  Your card has been added to the ATM!")


person1=ATM.atm(name,cardNumber,pin,expiryDate)
person1.depositToACC()
person1.withdrawFromACC()
person1.transactionHistory()
person1.balance()

