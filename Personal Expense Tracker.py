import json
from datetime import datetime

# Load expenses from file
def load_expenses(filename='expenses.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses, filename='expenses.json'):
    with open(filename, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., Food, Transport, etc.): ")
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ") or datetime.now().strftime("%Y-%m-%d")
    
    expenses.append({'amount': amount, 'category': category, 'date': date})
    save_expenses(expenses)
    print("Expense added successfully!")

# View expense summary
def view_summary(expenses):
    category = input("Enter category to view total spending (or press Enter for all): ")
    
    total = 0
    filtered_expenses = expenses if not category else [e for e in expenses if e['category'] == category]
    
    for expense in filtered_expenses:
        total += expense['amount']
    
    print(f"Total spending {'in ' + category if category else ''}: ${total:.2f}")

# Main menu
def main():
    expenses = load_expenses()

    while True:
        print("\n1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
