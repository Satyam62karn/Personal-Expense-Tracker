# Personal Expense Tracker

A Python-based expense management application that helps users record, organize, search, and analyze personal expenses. The project includes a command-line interface and a Streamlit web interface, with expense records stored in a CSV file.

## Features

* **Add Expenses:** Record expenses with a title, amount, category, and date.
* **View Expenses:** Display saved expense records.
* **Category Search:** Find expenses by category.
* **Total Calculation:** Calculate total spending.
* **Monthly Summary:** View expenses for a selected month.
* **Delete Expenses:** Remove an existing expense record.
* **CSV Data Storage:** Store expense records in a CSV file.
* **Input Validation:** Validate expense amounts and dates.
* **Dashboard:** View expense information through the Streamlit interface.
* **Data Visualization:** Display expense information using tables and charts.
* **Automated Testing:** Test core functionality using Python's `unittest` framework.

## Technologies Used

| Technology | Purpose                             |
| ---------- | ----------------------------------- |
| Python     | Application development             |
| Streamlit  | Web interface                       |
| Pandas     | Data handling and display           |
| CSV        | Expense data storage                |
| datetime   | Date handling and monthly summaries |
| unittest   | Automated testing                   |

## Project Structure

```text
Personal_Expense-Tracker/
│
├── main.py
├── app.py
├── expenses.csv
├── requirements.txt
├── README.md
├── .gitignore
│
└── tests/
    └── test_expenses.py
```

## Prerequisites

* Python 3.x
* pip
* A terminal or command-line interface
* A web browser for the Streamlit application

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Satyam62karn/Personal-Expense-Tracker.git
```

### 2. Open the Project Directory

```bash
cd Personal-Expense-Tracker
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

### Command-Line Application

Run the following command:

```bash
python main.py
```

### Streamlit Web Application

Run the following command:

```bash
python -m streamlit run app.py
```

The application will open in your browser. If it does not open automatically, use the local URL displayed in the terminal.

## Application Menu

| Option | Operation                |
| ------ | ------------------------ |
| 1      | Add Expense              |
| 2      | View All Expenses        |
| 3      | Search by Category       |
| 4      | Calculate Total Expenses |
| 5      | Monthly Expense Summary  |
| 6      | Delete an Expense        |
| 7      | Exit                     |

*The menu above describes the command-line application.*

## Date Formats

* **Expense Date:** `YYYY-MM-DD`
* **Monthly Summary:** `YYYY-MM`

Examples:

* Expense date: `2026-10-13`
* Monthly summary: `2026-10`

## Sample Expense Data

The following table represents previously verified sample expense records.

| Expense         |   Amount (₹) | Category      |
| --------------- | -----------: | ------------- |
| Lunch           |       120.00 | Food          |
| Tea             |        20.00 | Food          |
| Bus Fare        |        50.00 | Travel        |
| NoteBook        |       100.00 | Education     |
| Breakfast       |        60.00 | Food          |
| Mobile Recharge |       349.00 | Bills         |
| Movie Ticket    |       700.00 | Entertainment |
| **Total**       | **1,399.00** |               |

*Note: These sample records may differ from the current contents of `expenses.csv`.*

## Running Automated Tests

The project includes unit tests for expense creation, input validation, expense retrieval, total calculation, category searching, monthly summaries, and expense deletion.

Run the following command from the project directory:

```bash
python -m unittest discover -s tests -v
```

### Previously Verified Test Results

* Tests executed: 8
* Tests passed: 8
* Tests failed: 0

All eight tests passed in the previously verified test run. Run the command again to verify the current code.

## Data Storage

Expense records are stored in `expenses.csv` using the following fields:

* `title`
* `amount`
* `category`
* `date`

The CSV file stores expense records between local application runs.

**Note:** The deployed Streamlit version uses the application's file environment. CSV changes on a cloud deployment may not persist permanently across restarts or redeployments.

## Live Project

**Live Application:** https://personal-expense-tracker-satyam.streamlit.app/

## GitHub Repository

**Source Code:** https://github.com/Satyam62karn/Personal-Expense-Tracker

## Learning Outcomes

* Developed a command-line application using Python.
* Built a web interface using Streamlit.
* Practiced functions, conditional statements, loops, and file handling.
* Implemented CSV-based data storage.
* Applied input validation and date handling.
* Created automated unit tests using `unittest`.
* Organized source code, tests, and documentation.
* Learned the basics of deploying a Python application.

## Future Enhancements

* Add user authentication.
* Introduce budget limits and spending alerts.
* Export monthly summaries.
* Improve data persistence with a database.
* Add additional reports and visualizations.

## Author

**Satyam Kumar Karn**

---

*Personal Expense Tracker — A Python project focused on practical expense management, data analysis, and application development.*
