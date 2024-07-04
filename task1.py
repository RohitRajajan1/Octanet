import time as t

print("Please insert your card")
t.sleep(3)
pin = 1234
balance = 5000
transaction_history = []  # List to store transaction history
n = int(input("enter your atm pin : "))

if n == pin:
    while True:
        # Display ATM menu options
        print("Welcome to ATM")
        print("1. Account balance enquiry")
        print("2. Cash withdrawal")
        print("3. Cash deposit")
        print("4. Pin change")
        print("5. Transaction history")
        print("6. Exit")
        # Get user choice and handle invalid input
        try:
            option = int(input("please enter your choice : "))
        except:
            print("Please enter valid option : ")
            continue
        if option == 1:
            # Display current account balance
            print(f"Your current balance is :{balance}")
        elif option == 2:
            # Handle cash withdrawal
            wtdw_amt = int(input("please enter withdraw amount : "))
            balance = balance - wtdw_amt
            print(f"{wtdw_amt} amount is debited.")
            transaction_history.append(("Withdrawal", wtdw_amt, t.time()))
        elif option == 3:
            # Handle cash deposit
            dep_amt = int(input("please enter deposit amount : "))
            balance = balance + dep_amt
            print(f"{dep_amt} is credited to your account.")
            transaction_history.append(("Deposit", dep_amt, t.time()))
        elif option == 4:
            # Handle pin change
            pin_change = int(input("enter new pin"))
            pin = pin_change
            print("Pin Successfully Changed")
        elif option == 5:
            # Display transaction history
            print("Transaction history")
            for transaction in transaction_history:
                transaction_type, amount, timestamp = transaction
                print(f"{transaction_type} of {amount} on {t.ctime(timestamp)}")
        elif option == 6:
            # Exit the ATM menu
            print("Thank you for using the ATM.")
            print("Please Visit Again.")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Wrong Pin")
    print("Please enter the valid pin")
