import streamlit as st
import csv
import os
from datetime import datetime
import pandas as pd

FILE_NAME = "expenses.csv"
FIELDS = ["title", "amount", "category", "date"]

st.set_page_config(
    page_title="Personal Expense Tracker",
    page_icon="💰",
    layout="wide"
)


def get_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def save_expense(title, amount, category, date):
    expense = {
        "title": title.strip(),
        "amount": f"{amount:.2f}",
        "category": category.strip(),
        "date": date.strftime("%Y-%m-%d")
    }

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)

        if not file_exists or os.path.getsize(FILE_NAME) == 0:
            writer.writeheader()

        writer.writerow(expense)


def save_all_expenses(expenses):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(expenses)


st.title("💰 Personal Expense Tracker")
st.write("Manage, search, and track your daily expenses in one place.")

expenses = get_expenses()

total = sum(float(item["amount"]) for item in expenses)
col1, col2, col3 = st.columns(3)

col1.metric("Total Expenses", f"₹{total:,.2f}")
col2.metric("Total Records", len(expenses))
col3.metric(
    "Categories",
    len(set(item["category"].strip().lower() for item in expenses))
)

st.divider()

menu = st.sidebar.selectbox(
    "Choose an Option",
    [
        "Dashboard",
        "Add Expense",
        "View All Expenses",
        "Search by Category",
        "Calculate Total",
        "Monthly Summary",
        "Delete Expense"
    ]
)

if menu == "Dashboard":
    st.subheader("📊 Expense Dashboard")

    if expenses:
        df = pd.DataFrame(expenses)
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)

        st.write("### Recent Expenses")
        st.dataframe(df.tail(10).iloc[::-1], use_container_width=True)

        st.write("### Expenses by Category")
        category_totals = df.groupby("category")["amount"].sum()
        st.bar_chart(category_totals)
    else:
        st.info("No expenses yet. Select 'Add Expense' to get started.")

elif menu == "Add Expense":
    st.subheader("➕ Add a New Expense")

    with st.form("add_expense_form"):
        title = st.text_input("Expense Title")
        amount = st.number_input("Amount (₹)", min_value=0.0, step=10.0)
        category = st.text_input("Category")
        expense_date = st.date_input("Expense Date", value=datetime.today().date())

        submitted = st.form_submit_button("Save Expense")

        if submitted:
            if not title.strip():
                st.error("Expense title cannot be empty.")
            elif amount <= 0:
                st.error("Amount must be greater than zero.")
            elif not category.strip():
                st.error("Category cannot be empty.")
            else:
                save_expense(title, amount, category, expense_date)
                st.success("Expense added and saved successfully!")
                st.rerun()

elif menu == "View All Expenses":
    st.subheader("📋 All Expenses")

    if expenses:
        df = pd.DataFrame(expenses)
        st.dataframe(df, use_container_width=True)
        st.caption(f"Total records: {len(expenses)}")
    else:
        st.info("No expenses found.")

elif menu == "Search by Category":
    st.subheader("🔍 Search Expenses by Category")

    categories = sorted(set(
        item["category"] for item in expenses if item["category"].strip()
    ))

    if categories:
        selected_category = st.selectbox("Select Category", categories)

        results = [
            item for item in expenses
            if item["category"].strip().lower()
            == selected_category.strip().lower()
        ]

        st.dataframe(pd.DataFrame(results), use_container_width=True)
        st.write(f"Matching expenses: {len(results)}")
    else:
        st.info("No categories available yet.")

elif menu == "Calculate Total":
    st.subheader("🧮 Total Expenses")
    st.metric("Total Amount Spent", f"₹{total:,.2f}")

    if expenses:
        df = pd.DataFrame(expenses)
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)
        st.write("### Category-wise Total")
        st.bar_chart(df.groupby("category")["amount"].sum())

elif menu == "Monthly Summary":
    st.subheader("📅 Monthly Expense Summary")

    selected_month = st.text_input(
        "Enter Month (YYYY-MM)",
        value=datetime.today().strftime("%Y-%m")
    )

    if st.button("Show Monthly Summary"):
        try:
            datetime.strptime(selected_month, "%Y-%m")

            monthly_expenses = [
                item for item in expenses
                if item["date"].startswith(selected_month)
            ]

            if monthly_expenses:
                monthly_total = sum(
                    float(item["amount"]) for item in monthly_expenses
                )

                st.metric("Monthly Total", f"₹{monthly_total:,.2f}")
                st.write(f"Number of expenses: {len(monthly_expenses)}")
                st.dataframe(
                    pd.DataFrame(monthly_expenses),
                    use_container_width=True
                )
            else:
                st.info("No expenses found for this month.")

        except ValueError:
            st.error("Invalid month. Please use YYYY-MM format.")

elif menu == "Delete Expense":
    st.subheader("🗑️ Delete an Expense")

    if expenses:
        options = list(range(len(expenses)))

        selected_index = st.selectbox(
            "Select Expense",
            options,
            format_func=lambda i: (
                f"{i + 1}. {expenses[i]['title']} | "
                f"₹{expenses[i]['amount']} | "
                f"{expenses[i]['category']} | "
                f"{expenses[i]['date']}"
            )
        )

        confirm = st.checkbox("I confirm that I want to delete this expense.")

        if st.button("Delete Selected Expense", type="primary"):
            if confirm:
                expenses.pop(selected_index)
                save_all_expenses(expenses)
                st.success("Expense deleted successfully!")
                st.rerun()
            else:
                st.warning("Please confirm before deleting.")
    else:
        st.info("No expenses available to delete.")

st.divider()
st.caption("Personal Expense Tracker | Python • Streamlit • CSV")