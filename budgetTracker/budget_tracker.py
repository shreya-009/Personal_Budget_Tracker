from transaction import Transaction
import calendar
import datetime

def main():
    print(f"🎯 Running Personal Budget Tracker!")
    transaction_file_path = "transactions.csv"

    while True:
        print("\n1. Enter Income\n2. Enter Expense\n3. View Month-Wise Expenses\n4. Analyze Category-Wise Expenses\n5. Calculate Budget\n6. Exit")
        choice = input("Enter Your Choice: ")

        if choice == "1":
            # Get User input for income.
            income = get_user_income()
            # Write their income to a file
            save_income_to_file(income, transaction_file_path)
            print("Income Saved Successfully.")
        elif choice == "2":
            # Get user input for expense.
            expense = get_user_expense()
            # Write their expense to a file
            save_expense_to_file(expense, transaction_file_path)
            print("Expense Saved Successfully.")
        elif choice == "3":
            # Read transactions from the file.
            transactions = read_transactions_from_file(transaction_file_path)
            # view Month-Wise Expenses only
            view_month_wise_expenses(transactions)
        elif choice == "4":
            transactions = read_transactions_from_file(transaction_file_path)
            analyze_category_wise_expenses(transactions)
        elif choice == "5":
            # Read transactions from the file
            transactions = read_transactions_from_file(transaction_file_path)
            # calculate the budget remaining after reading the file
            budget = calculate_budget(transactions)
            print(green(f"Budget Remaining: ${budget:.2f}"))
        elif choice == "6":
            break

def get_user_income():
    print(f"🎯 Getting User Income")
    income_name = input("Enter income name: ")
    income_amount = float(input("Enter income amount: "))
    income_category = None
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    transaction = Transaction(name=income_name, category=income_category, amount=income_amount, transaction_type='Income', date=date)
    
    return transaction


def get_user_expense():
    print(f"🎯 Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    
   
    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
    ]

    selected_category = None
    while selected_category is None:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            
        else:
            print("Invalid category. Please try again!")

    date = datetime.datetime.now().strftime('%Y-%m-%d')
    transaction = Transaction(expense_name, selected_category, expense_amount, 'Expense', date)
    
    return transaction

def save_income_to_file(income: Transaction, transaction_file_path):
    print(f"🎯 Saving User Income: {income} to {transaction_file_path}")
    with open(transaction_file_path, mode="a", encoding="utf-8") as f: 
        f.write(f"{income.name},{income.amount},{income.category},{income.transaction_type},{income.date}\n")


def save_expense_to_file(expense: Transaction, transaction_file_path):
    print(f"🎯 Saving User Expense: {expense} to {transaction_file_path}")
    with open(transaction_file_path, mode="a", encoding="utf-8") as f: 
        f.write(f"{expense.name},{expense.amount},{expense.category},{expense.transaction_type},{expense.date}\n")

def read_transactions_from_file(transaction_file_path):
    transactions = []
    with open(transaction_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            name, amount, category, transaction_type, date = line.strip().split(",")
            transaction = Transaction(name, category, float(amount), transaction_type, date)
            transactions.append(transaction)
    return transactions

def calculate_budget(transactions):
    print("👉 Budget Calculation is : ")
    total_income = sum([t.amount for t in transactions if t.transaction_type == 'Income'])
    print(f"💵 Total income: ${total_income:.2f}")
    total_expenses = sum([t.amount for t in transactions if t.transaction_type == 'Expense'])
    print(f"💵 Total spent: ${total_expenses:.2f}")
    return total_income - total_expenses

def view_month_wise_expenses(transactions):
    print("🎯 Viewing Month-Wise Expenses: ")
    month_name = input("Enter the month name (e.g., January, February, etc.): ").strip()
    month = datetime.datetime.strptime(month_name, '%B').month

    total_expenses = 0
    expenses_exist = False

    for transaction in transactions:
        transaction_date = datetime.datetime.strptime(transaction.date, '%Y-%m-%d')
        if transaction_date.month == month and transaction.transaction_type == 'Expense':
            total_expenses += transaction.amount
            expenses_exist = True

    if expenses_exist:
        print(green(f"Total expenses for {month_name}: ${total_expenses:.2f}"))
    else:
        print(f"No expenses for {month_name}.")

def analyze_category_wise_expenses(transactions):
    category_expenses = {}

    for transaction in transactions:
        if transaction.transaction_type == 'Expense':
            if transaction.category in category_expenses:
                category_expenses[transaction.category] += transaction.amount
            else:
                category_expenses[transaction.category] = transaction.amount

    if category_expenses:
        print("📊 Category-Wise Expenses Analysis:")
        for category, amount in category_expenses.items():
            print(f"  {category}: ${amount:.2f}")
    else:
        print("No expenses to analyze.")



def green(text):
    return f"\033[92m{text}\033[0m"
   

if __name__ == "__main__":
    main()
