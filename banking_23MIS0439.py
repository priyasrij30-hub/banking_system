balance = 1000
history = []

while True:
    print("\n1.Check Balance  2.Deposit  3.Withdraw  4.History  5.Exit")
    choice = input("Choice: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amt = int(input("Enter amount: "))
        balance += amt
        history.append(f"Deposited {amt}")
        print("Amount deposited")

    elif choice == "3":
        amt = int(input("Enter amount: "))
        if amt <= balance:
            balance -= amt
            history.append(f"Withdrawn {amt}")
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    elif choice == "4":
        print("Transaction History:")
        for h in history:
            print("-", h)

    elif choice == "5":
        break

    else:
        print("Invalid choice")
