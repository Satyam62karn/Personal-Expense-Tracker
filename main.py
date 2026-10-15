
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"
FIELDS = ["title", "amount", "category", "date"]

def get_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

def add_expense():
    print("\n----- ADD EXPENSE -----")

    title = input("Enter expense title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid amount.")
        return

    category = input("Enter category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    date = input("Enter date (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return

    expense = {
        "title": title,
        "amount": f"{amount:.2f}",
        "category": category,
        "date": date
    }

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writeheader()

        writer.writerow(expense)

    print("Expense added and saved successfully!")

def view_expenses():
    print("\n----- ALL EXPENSES -----")
    expenses = get_expenses()

    if not expenses:
        print("No expenses found.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense {index}")
        print("Title:", expense["title"])
        print("Amount: Rs.", expense["amount"])
        print("Category:", expense["category"])
        print("Date:", expense["date"])

    print("\nTotal records:", len(expenses))

def search_by_category():
    print("\n----- SEARCH BY CATEGORY -----")
    category = input("Enter category to search: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    expenses = get_expenses()
    results = [
        expense for expense in expenses
        if expense["category"].strip().lower() == category.lower()
    ]

    if not results:
        print("No expenses found in this category.")
        return

    for expense in results:
        print("--------------------------")
        print("Title:", expense["title"])
        print("Amount: Rs.", expense["amount"])
        print("Category:", expense["category"])
        print("Date:", expense["date"])

    print("--------------------------")
    print("Matching expenses:", len(results))

def calculate_total():
    print("\n----- TOTAL EXPENSES -----")
    expenses = get_expenses()
    total = sum(float(expense["amount"]) for expense in expenses)
    print(f"Total Expenses: Rs. {total:.2f}")

def monthly_summary():
    print("\n----- MONTHLY EXPENSE SUMMARY -----")
    month = input("Enter month (YYYY-MM): ").strip()

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month. Use YYYY-MM.")
        return

    expenses = get_expenses()
    monthly_expenses = [
        expense for expense in expenses
        if expense["date"].startswith(month)
    ]

    if not monthly_expenses:
        print("No expenses found for this month.")
        return

    total = sum(float(expense["amount"]) for expense in monthly_expenses)
    print("Month:", month)
    print("Number of expenses:", len(monthly_expenses))
    print(f"Total expenses: Rs. {total:.2f}")

def delete_expense():
    print("\n----- DELETE EXPENSE -----")
    expenses = get_expenses()

    if not expenses:
        print("No expenses available to delete.")
        return

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['title']} | "
            f"Rs. {expense['amount']} | "
            f"{expense['category']} | {expense['date']}"
        )

    try:
        choice = int(input("Enter expense number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if choice < 1 or choice > len(expenses):
        print("Invalid expense number.")
        return

    selected = expenses[choice - 1]
    confirm = input(
        f"Delete '{selected['title']}'? (yes/no): "
    ).strip().lower()

    if confirm != "yes":
        print("Deletion cancelled.")
        return

    expenses.pop(choice - 1)

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(expenses)

    print("Expense deleted successfully!")

def show_menu():
    print("\n==============================")
    print("   PERSONAL EXPENSE TRACKER")
    print("==============================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search by Category")
    print("4. Calculate Total Expenses")
    print("5. Monthly Expense Summary")
    print("6. Delete an Expense")
    print("7. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_by_category()
        elif choice == "4":
            calculate_total()
        elif choice == "5":
            monthly_summary()
        elif choice == "6":
            delete_expense()
        elif choice == "7":
            print("Thank you for using Personal Expense Tracker!")
            break
        else:
            print("Invalid choice! Please select 1-7.")

if __name__ == "__main__":
    main()