balance=int(input())
choice=int(input("enter your choice"))
i=0
while i<=0:
    if choice==1:
        print("check balance")
        print("available balalnce:",balance)
        i+=1
    elif choice==2:
        print("withdraw")
        ammount=int(input())
        if ammount<=balance:
            balance=balance-ammount
            print("transaction successfull")
            print("withdraw ammount:",ammount)
            print("remaining balance:",balance)
            print("thank you visit again")
        else:
            print("insufficient balance")
    elif choice==3:
        print("deposit")
        deposit=int(input())
        balance=balance+deposit
        print("deposit successfull")
        print("current balance:",balance)
        print("thank you visit agian")
    else:
        print("invalid choice")
    i+=1