import json
import os
from datetime import datetime


class Expense:
    def __init__(self, title, amount, date):
        self.title = title
        self.amount = amount
        self.date = date  # format: YYYY-MM-DD

    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "date": self.date
        }


class ExpenseTracker:
    FILE = "expenses.json"

    def __init__(self):
        if not os.path.exists(self.FILE):
            with open(self.FILE, "w") as f:
                json.dump([], f)

    def load_expenses(self):
        with open(self.FILE, "r") as f:
            return json.load(f)

    def save_expenses(self, expenses):
        with open(self.FILE, "w") as f:
            json.dump(expenses, f, indent=4)

    def add_expense(self, title, amount, date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD.")
            return

        try:
            amount = float(amount)
        except ValueError:
            print("❌ Amount must be a number.")
            return

        expenses = self.load_expenses()
        new_expense = Expense(title, amount, date)
        expenses.append(new_expense.to_dict())
        self.save_expenses(expenses)
        print("✅ Expense added successfully!")

    def view_all(self):
        expenses = self.load_expenses()

        if not expenses:
            print("No expenses found.")
            return

        print("\n------ All Expenses ------")
        for e in expenses:
            print(f"{e['date']} | {e['title']} | Rs. {e['amount']}")

    def total_expense(self):
        expenses = self.load_expenses()
        total = sum(e["amount"] for e in expenses)
        print(f"\n💰 Total Expense: Rs. {total}")

    def filter_by_date(self, date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("❌ Invalid date format.")
            return

        expenses = self.load_expenses()
        filtered = [e for e in expenses if e["date"] == date]

        if not filtered:
            print("No expenses found on this date.")
            return

        print(f"\n------ Expenses on {date} ------")
        for e in filtered:
            print(f"{e['title']} | Rs. {e['amount']}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expense")
        print("4. Filter by Date")
        print("5. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            title = input("Title: ")
            amount = input("Amount: ")
            date = input("Date (YYYY-MM-DD): ")
            tracker.add_expense(title, amount, date)

        elif choice == "2":
            tracker.view_all()

        elif choice == "3":
            tracker.total_expense()

        elif choice == "4":
            date = input("Enter date (YYYY-MM-DD): ")
            tracker.filter_by_date(date)

        elif choice == "5":
            print("👋 Exiting program...")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
