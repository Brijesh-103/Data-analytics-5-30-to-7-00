def bank(): 
    balance = 10000
    user_pin = int(input("Enter your pin: ")) 
    if user_pin == 1234:
        print("============BI Bank============\n")
        print("Wellcome Mr. Brijesh Shekhda", "\nYour current Account Number is: ", 123456789,"\nBank Name: BI Bank  ","\nYour current balance is: ", balance)
        print("Enter 1 For Check Balance", "\nEnter 2 For  Withdraw")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Your current balance is: ", balance,"\n")
            print("============= Thank You ============")
        elif choice == 2:  
            withdraw_amount = int(input("Enter the amount you want to withdraw: "))
            if withdraw_amount > balance:
                print("Insufficient balance \n")
                print("============= Thank You ============")
            else:
                balance -= withdraw_amount
                print("You have withdrawn: ", withdraw_amount, "\nYour current balance is: ", balance,"\n")
                print("============= Thank You ============")
        else:
            print("Invalid choice \n")
            print("============= Thank You ============")

    else:
        print("Invalid Pin \n")
        print("============= Thank You ============")
        return
    
bank()