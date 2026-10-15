# Personal Expense Tracker

A Python-based command-line application designed to record, manage, and analyze personal expenses. The application provides expense tracking, category-based searching, monthly summaries, and expense deletion, with data stored persistently in a CSV file.

## Features

- **Add Expenses:** Record expenses with a title, amount, category, and date.
- **View Expenses:** Display all saved expense records.
- **Category Search:** Find expenses by category.
- **Total Calculation:** Calculate the total amount spent.
- **Monthly Summary:** View expense statistics for a selected month.
- **Delete Expenses:** Remove an existing expense record.
- **CSV Data Storage:** Store expense records in a CSV file for future use.
- **Input Validation:** Validate expense amounts and dates.
- **Automated Testing:** Verify core functionality using Python's `unittest` framework.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| CSV | Expense data storage |
| datetime | Date handling and monthly summaries |
| unittest | Automated testing |

## Project Structure

```text
Personal_Expense-Tracker/
│
├── main.py
├── expenses.csv
├── README.md
│
└── tests/
    └── test_expenses.py
```

## Prerequisites

- Python 3.x
- A terminal or command-line interface

## Installation and Execution

### 1. Open the Project Directory

Open a terminal and navigate to the project folder.

### 2. Run the Application

Execute the following command:

```bash
python main.py
```

### 3. Select an Operation

Use the interactive menu to manage expenses.

## Application Menu

| Option | Operation |
|---|---|
| 1 | Add Expense |
| 2 | View All Expenses |
| 3 | Search by Category |
| 4 | Calculate Total Expenses |
| 5 | Monthly Expense Summary |
| 6 | Delete an Expense |
| 7 | Exit |

## Date Formats

- **Expense Date:** `YYYY-MM-DD`
- **Monthly Summary:** `YYYY-MM`

Examples:

- Expense date: `2026-10-13`
- Monthly summary: `2026-10`

## Sample Expense Data

The current `expenses.csv` file contains seven expense records.

| Expense | Amount (₹) | Category |
|---|---:|---|
| Lunch | 120.00 | Food |
| Tea | 20.00 | Food |
| Bus Fare | 50.00 | Travel |
| NoteBook | 100.00 | Education |
| Breakfast | 60.00 | Food |
| Mobile Recharge | 349.00 | Bills |
| Movie Ticket | 700.00 | Entertainment |
| **Total** | **1,399.00** | |

*The table reflects the expense records previously verified in the project.*

## Running Automated Tests

The project includes unit tests for expense creation, input validation, expense retrieval, total calculation, category searching, monthly summaries, and expense deletion.

Run the following command from the project directory:

```bash
python -m unittest discover -s tests -v
```

### Test Results

**Latest verified result:**

- Tests executed: 8
- Tests passed: 8
- Tests failed: 0

All eight tests passed in the latest test run.

## Data Storage

Expense records are stored in `expenses.csv` using the following fields:

- `title`
- `amount`
- `category`
- `date`

The CSV file enables the application to retain expense records between executions.

## Learning Outcomes

- Developed a command-line application using Python.
- Practiced functions, conditional statements, and loops.
- Implemented CSV file handling for persistent data storage.
- Applied input validation and date handling.
- Created automated unit tests using `unittest`.
- Organized code and tests into a structured project.

## Future Enhancements

- Add graphical user interface support.
- Generate expense reports and visualizations.
- Export monthly summaries.
- Add budget limits and spending alerts.

## Author

**Satyam Kumar Karn**

---

*Personal Expense Tracker — A Python project focused on practical expense management and automated testing.*