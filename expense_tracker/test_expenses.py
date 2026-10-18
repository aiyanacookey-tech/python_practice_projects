def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense['amount']      
    return total

test_expenses = [
    {'name': 'Coffee', 'amount': 4.50},
    {'name': 'Lunch', 'amount': 12.00},
    {'name': 'Transport', 'amount': 3.50}
]

assert calculate_total(test_expenses) == 20.0
print("Test 1 passed!")