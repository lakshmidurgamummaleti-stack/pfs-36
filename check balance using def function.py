balance = int(input("Enter balance: "))
def check_balance():
    print("Available balance:", balance)
def withdraw():
    global balance
    amount = int(input("Enter withdraw amount: "))
    if amount <= balance:
        balance -= amount
        print("Transaction successful")
        print("Withdraw amount:", amount)
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")
def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))
    balance += amount
    print("Deposit successful")
    print("Current balance:", balance)
def atm():
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            check_balance()
        elif choice == 2:
            withdraw()
        elif choice == 3:
            deposit()
        elif choice == 4:
            print("Thank you, visit again!")
            break
        else:
            print("Invalid choice")
atm()