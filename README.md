# Personal Expense Tracker

A simple command-line Personal Expense Tracker built with Python. The application allows users to record, view, categorize, save, and analyze their expenses. It also provides graphical visualizations of category-wise and monthly spending.

## Features

* Add expenses with amount, category, and date.
* Supported categories:

  * Food
  * Transport
  * Entertainment
* Validate expense amounts and reject invalid or non-positive values.
* Validate dates using the `YYYY-MM-DD` format.
* View all recorded expenses in a structured table.
* Generate an expense report containing:

  * Total spending
  * Category-wise spending
  * Monthly spending
  * Highest expense
* Save expenses to a CSV file.
* Load previously saved expenses when the program starts.
* Generate a bar chart for category-wise spending.
* Generate a bar chart for monthly spending.
* Handle invalid user input using `try-except`.
* Use a menu-driven command-line interface.

## Technologies Used

* Python
* CSV module
* `datetime` module
* Matplotlib

## Project Structure

```text
PERSONAL_EXPENSE_TRACKER/
│
├── .venv/
├── expense_tracker.py
├── expenses.csv
├── requirements.txt
├── .gitignore
└── README.md
```

### File Description

* `expense_tracker.py` — Main Python application.
* `expenses.csv` — Stores saved expense records.
* `requirements.txt` — Contains the required external Python package.
* `.gitignore` — Prevents unnecessary files such as the virtual environment and Python cache files from being tracked.
* `README.md` — Project documentation.
* `.venv/` — Local Python virtual environment used for the project.

## Requirements

* Python 3.x
* Matplotlib

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Open the project folder

```bash
cd PERSONAL_EXPENSE_TRACKER
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

On Windows:

```bash
.venv\Scripts\activate
```

### 5. Install the required package

```bash
pip install -r requirements.txt
```

## Running the Application

Run the following command from the project folder:

```bash
python expense_tracker.py
```

The application will display a menu similar to:

```text
===== Personal Expense Tracker =====
1. Add an Expense
2. View All Expenses
3. Generate Report
4. Show Category Spending Chart
5. Show Monthly Spending Chart
6. Save and Exit
```

Select an option by entering its corresponding number.

## Data Storage

Expense records are stored in `expenses.csv`.

When the application starts, previously saved expenses are loaded automatically. When the user selects **Save and Exit**, the current expenses are written to the CSV file.

## Reports and Visualization

The application generates:

* Total spending
* Category-wise spending
* Monthly spending
* Highest expense

It also provides two Matplotlib bar charts:

1. Category-wise Spending
2. Monthly Spending

## Error Handling

The application uses `try-except` to handle invalid numerical input and CSV loading problems. It also validates expense categories and dates before adding an expense.

## Future Improvements

Possible future improvements include:

* Additional expense categories
* Weekly spending reports
* Expense editing and deletion
* Search and filtering options
* Budget tracking
* More advanced visualizations
* Exporting reports to other formats

## Author

**Subhadip Maity**

BTech Computer Science and Engineering Student
