expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expenses")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        expense_name = input("Enter expense name: ")
        expense_amount = float(input("Enter amount: ")) 

        expense = {
            'name': expense_name,
            'amount': expense_amount
        }

        expenses.append(expense)

        print("Expense added successfully.")
        
    elif choice == '2':
         print("Viewing Expenses:")

         # Challenge to display the expenses 
         for expense in expenses:
             print(f"Expense Name: {expense['name']}, Amount: {expense['amount']}")

    
    elif choice == '3':
            print("Calculating Total Expenses:")


    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")

    

