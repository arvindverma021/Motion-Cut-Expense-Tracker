import sys
from expense_manager import add_expense, view_expenses
from reports import monthly_summary, category_summary


def display_menu():
    """Displays the menu options."""
    print("\n💰 Expense Tracker")
    print("1️⃣ Add Expense")
    print("2️⃣ View Expenses")
    print("3️⃣ Monthly Summary")
    print("4️⃣ Category-wise Summary")
    print("5️⃣ Exit")


def main():
    """Runs the Expense Tracker CLI."""
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            date = input("Enter Date (YYYY-MM-DD): ")
            amount = float(input("Enter Amount: "))
            category = input("Enter Category (Food, Transport, Entertainment, Bills, Others): ")
            description = input("Enter Description: ")
            add_expense(date, amount, category, description)

        elif choice == "2":
            expenses = view_expenses()
            print("\n📜 Expense List:")
            for exp in expenses:
                print(f"{exp[1]} | ${exp[2]:.2f} | {exp[3]} | {exp[4]}")

        elif choice == "3":
            monthly_summary()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("Exiting... 👋")
            sys.exit()

        else:
            print("❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
