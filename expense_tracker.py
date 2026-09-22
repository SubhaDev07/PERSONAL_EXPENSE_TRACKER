import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Its Stores All ExPenses dUring the current program session.
expenses = []

def add_expense():
    try:
       amount = float(input("Enter expense amount: "))

# to ignore 0 and negative numbers beacuse expense shoul be all time positive
       if amount <= 0:
        print("Invalid amount. Please enter a positive number.")
        return

    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    # Normalize the category so inputs like ex: "food" and " FOOD " both can be accepted
    category = input("Enter expense category (Food/Transport/Entertainment): ").strip().title()

   
#  to ignore empty inputs for category
    if not category:
      print("Category cannot be empty.")
      return

#  Restrict other keywords rather than "food" , "Transport" and "entertainment"
    if category not in ["Food", "Transport", "Entertainment"]: 
        print("Invalid category. Please choose Food, Transport, or Entertainment.")
        return
    
    date = input("Enter expense date (YYYY-MM-DD): ").strip()

#  This prevents invalid dates format from entering the dataset.
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
       print("Invalid date. Please use YYYY-MM-DD format.")
       return

# Keep each expense in a structured format so it can be 
#  easily processed by reports, charts, and CSV storage.
    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)

    print("Expense added successfully!")

# view all expenses given by the user 

def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

# for output alignment .Basically here  we are using this to align the price structure.
    print(f"\n{'Date':<12}{'Category':<18}{'Amount':>12}")
    print("-" * 45)

    for expense in expenses:
        print(
            f"{expense['date']:<12}"
            f"{expense['category']:<18}"
            f"₹{expense['amount']:>11.2f}"
)


# Generate expense report
def generate_report():
    if not expenses:
        print("No expenses found.")
        return

# Calculate the total amount spent 
    total_spending = sum(expense["amount"] for expense in expenses)

    print("\n===== Expense Report =====")
    print(f"Total Spending: ₹{total_spending:.2f}")

#  to understand where most money is spent Aggregating expenses by category
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\nCategory-wise Spending:")
    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")

# This gives us a simple way to group expenses by month.
# The date : YYYY-MM-DD represent YYYY-MM here in monthly totals.

    monthly_totals = {}

    for expense in expenses:
        month = expense["date"][:7]
        amount = expense["amount"]

        if month in monthly_totals:
            monthly_totals[month] += amount
        else:
            monthly_totals[month] = amount

    print("\nMonthly Spending:")
    for month, amount in monthly_totals.items():
        print(f"{month}: ₹{amount:.2f}")

 # to find highest expense
    highest_expense = max(expenses, key=lambda expense: expense["amount"])
    print("\nHighest Expense:")
    print(
          f"{highest_expense['date']} - "
          f"{highest_expense['category']} - "
          f"₹{highest_expense['amount']:.2f}"
    )
    


# Visualize category-wise spending
def plot_category_spending():
    if not expenses:
        print("No expenses available for visualization.")
        return

#  we are using aggreting function again to preapre data for the chart
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())


# A bar chart makes it easier to compare spending across categories.
    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts)
    plt.xlabel("Category")
    plt.ylabel("Amount Spent (₹)")
    plt.title("Category-wise Spending")
    plt.tight_layout()
    plt.show()


# Visualize monthly spending

def plot_monthly_spending():
    if not expenses:
        print("No expenses available for visualization.")
        return
# Group all expenses by YYYY-MM before passing the data to Matplotlib.
    monthly_totals = {}

    for expense in expenses:
        month = expense["date"][:7]
        amount = expense["amount"]

        if month in monthly_totals:
            monthly_totals[month] += amount
        else:
            monthly_totals[month] = amount

    months = list(monthly_totals.keys())
    amounts = list(monthly_totals.values())

# Visualizing monthly totals for identify changes in spending over time.
    plt.figure(figsize=(8, 5))
    plt.bar(months, amounts)
    plt.xlabel("Month")
    plt.ylabel("Amount Spent (₹)")
    plt.title("Monthly Spending")
    plt.tight_layout()
    plt.show()


# Save expenses to CSV
def save_expenses():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["amount", "category", "date"])
        writer.writeheader()
        writer.writerows(expenses)

    print("Expenses saved successfully!")


# Load expenses from CSV
def load_expenses():
    try:
        with open("expenses.csv", "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    row["amount"] = float(row["amount"])
                    expenses.append(row)
                except (ValueError, KeyError):
                    print("Warning: Invalid expense data found in CSV. Skipping that entry.")

    except FileNotFoundError:
        pass

# Restore previously saved expenses before displaying the main menu.
load_expenses()

# Main Menu
# main menu is always running until user choose 6 save and exit.
while True:
    print("\n===== Personal Expense Tracker =====")
    print("1. Add an Expense")
    print("2. View All Expenses")
    print("3. Generate Report")
    print("4. Show Category Spending Chart")
    print("5. Show Monthly Spending Chart")
    print("6. Save and Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        generate_report()
    elif choice == "4":
        plot_category_spending()
    elif choice == "5":
        plot_monthly_spending()
    elif choice == "6":
        save_expenses() # by using this function we can save it into the expenses.csv
        print("Thank you for using Personal Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")

