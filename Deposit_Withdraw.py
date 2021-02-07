NetAmount=0

while True:
    userChoice=str(input("Press D for Deposit, W for withdraw or Q for quit: "))

        
    if userChoice == 'D':
        amount= int(input("Enter amount you want to deposit: "))
        print(f"D ={amount}")
        NetAmount+= amount

    elif userChoice == 'W':
        amount= int(input("Enter amount you want to dDeposit: "))
        print(f"W ={amount}")
        NetAmount-=amount

    elif userChoice == 'Q':
        print(f"Net Amount ={NetAmount}")
        break
