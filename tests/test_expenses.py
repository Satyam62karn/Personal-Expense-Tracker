import csv
import os
import tempfile
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO

import main


class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        # Create a temporary CSV file for testing
        temp = tempfile.NamedTemporaryFile(
            mode="w",
            newline="",
            suffix=".csv",
            delete=False,
            encoding="utf-8"
        )
        temp.close()

        self.file_path = temp.name

        # Add sample expenses
        with open(
            self.file_path, "w", newline="", encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(
                file, fieldnames=main.FIELDS
            )
            writer.writeheader()

            writer.writerow({
                "title": "Lunch",
                "amount": "120.00",
                "category": "Food",
                "date": "2026-10-13"
            })

            writer.writerow({
                "title": "Bus",
                "amount": "30.00",
                "category": "Travel",
                "date": "2026-10-12"
            })

        # Make the application use the temporary CSV file
        self.file_patch = patch(
            "main.FILE_NAME", self.file_path
        )
        self.file_patch.start()
        self.addCleanup(self.file_patch.stop)

    def tearDown(self):
        # Remove the temporary CSV file
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    # Test 1: Read expenses
    def test_get_expenses(self):
        expenses = main.get_expenses()

        self.assertEqual(len(expenses), 2)
        self.assertEqual(expenses[0]["title"], "Lunch")

    # Test 2: Calculate total
    def test_calculate_total(self):
        output = StringIO()

        with redirect_stdout(output):
            main.calculate_total()

        self.assertIn("150.00", output.getvalue())

    # Test 3: Search by category
    def test_search_by_category(self):
        output = StringIO()

        with patch("builtins.input", return_value="Food"):
            with redirect_stdout(output):
                main.search_by_category()

        result = output.getvalue()

        self.assertIn("Lunch", result)
        self.assertIn("Matching expenses: 1", result)

    # Test 4: Monthly summary
    def test_monthly_summary(self):
        output = StringIO()

        with patch("builtins.input", return_value="2026-10"):
            with redirect_stdout(output):
                main.monthly_summary()

        result = output.getvalue()

        self.assertIn("Number of expenses: 2", result)
        self.assertIn("Total expenses: Rs. 150.00", result)

    # Test 5: Add a new expense
    def test_add_expense(self):
        user_inputs = [
            "Dinner",
            "250",
            "Food",
            "2026-10-13"
        ]

        with patch("builtins.input", side_effect=user_inputs):
            main.add_expense()

        expenses = main.get_expenses()

        self.assertEqual(len(expenses), 3)
        self.assertEqual(expenses[2]["title"], "Dinner")
        self.assertEqual(expenses[2]["amount"], "250.00")
        self.assertEqual(expenses[2]["category"], "Food")

    # Test 6: Delete an expense
    def test_delete_expense(self):
        user_inputs = ["2", "yes"]

        with patch("builtins.input", side_effect=user_inputs):
            main.delete_expense()

        expenses = main.get_expenses()

        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0]["title"], "Lunch")

    # Test 7: Reject an invalid amount
    def test_add_expense_invalid_amount(self):
        user_inputs = ["Dinner", "abc"]

        output = StringIO()

        with patch("builtins.input", side_effect=user_inputs):
            with redirect_stdout(output):
                main.add_expense()

        self.assertIn(
            "Please enter a valid amount.",
            output.getvalue()
        )

        expenses = main.get_expenses()
        self.assertEqual(len(expenses), 2)

    # Test 8: Reject an invalid date
    def test_add_expense_invalid_date(self):
        user_inputs = [
            "Dinner",
            "250",
            "Food",
            "13-10-2026"
        ]

        output = StringIO()

        with patch("builtins.input", side_effect=user_inputs):
            with redirect_stdout(output):
                main.add_expense()

        self.assertIn(
            "Invalid date. Use YYYY-MM-DD.",
            output.getvalue()
        )

        expenses = main.get_expenses()
        self.assertEqual(len(expenses), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)