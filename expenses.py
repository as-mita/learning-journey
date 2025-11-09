# 🧾 Simple Expense Tracker
# This script lets you add, view, and calculate total expenses.

expenses = []

def add_expense():
    """Add a new expense with name and amount"""
    name = input("Enter expense name: ")
    amount = float(input("Enter amount (in NPR): "))
    expenses.append({"name": name, "amount": amount})
    print(f"Expense '{name}' of NPR {amount} added!\n")

def view_expenses():
    """View all recorded expenses"""
    if not expenses:
        print(" No expenses recorded yet.\n")
        return
    print("\n--- Expense List ---")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - NPR {expense['amount']}")
    print()

def total_expenses():
    """Calculate and display total expenses"""
    total = sum(item["amount"] for item in expenses)
    print(f" Total Expenses: NPR {total}\n")

def main():
    print("Welcome to Your Expense Tracker \n")
    while True:
        print("Choose an option:")
        print(" 1 dd Expense")
        print(" 2 View Expenses")
        print(" 3 Show Total")
        print(" 4 Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            print(" Exiting... Have a great day!")
            break
        else:
            print(" Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
