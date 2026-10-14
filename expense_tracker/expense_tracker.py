expenses = [] # represents a list, whereas expense ={} represents a dictionary. A list can hold multiple items, while a dictionary holds key-value pairs.

def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense['amount']      
        return total

while True: # creates a loop that runs continuously until something explicitly stops it, usually break
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expenses")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        expense_name = input("Enter expense name: ")

        while True:
            try:
                expense_amount = float(input("Enter expense amount: "))

                if expense_amount <= 0:
                    print("Amount must be a positive number. Please try again")
                else:
                    break
            except ValueError: 
                print("Invalid input. Please enter a valid number.")
            
        expense = {
            'name': expense_name,
            'amount': expense_amount
        }

        expenses.append(expense)

        print("Expense added successfully.")
        
    elif choice == '2':
         print("Viewing Expenses:")

         # Challenge to display the expenses 
         if len(expenses) == 0:
                 print("No expenses to display.")
         else:
              for expense in expenses:
                    print(f"Expense Name: {expense['name']}, Amount: {expense['amount']}")
        
    
    elif choice == '3':
            print("Calculating Total Expenses:")
            total = calculate_total(expenses)
            print(f"Total Expenses: {total}")


    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")

    

