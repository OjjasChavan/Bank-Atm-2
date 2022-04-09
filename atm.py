balance = 100

name = input("Enter your name: ")

print("Hello,",name,"!")

card_no = int(input("Enter your Card Number: "))
card_pin = int(input("Enter your Card PIN: "))

activity = int(input("1. Balance Inquiry \n2. Cash Withdrawl \nEnter your activity number: "))

if activity == 1:
    print("You chose Balance Inquiry \nYour balance is: $", balance)
elif activity == 2:
    print("You chose Cash Withdrawl")
    amount = int(input("Enter the amount you want to withdraw: "))
    if amount > balance:
        print("Insufficient funds")
    else:
        print("Withdrawal successful")
        balance = balance - amount
        print("Your new balance is: $", balance)
else:
    print("Invalid activity")