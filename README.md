# Motion-Cut-Expense-TrackerExpense Tracker Project - Overview
The Expense Tracker is a Python-based application that helps users manage and analyze their daily expenses. It allows users to record expenses, categorize them, and generate reports to track their spending habits over time.

🎯 Objectives
Record daily expenses (amount, category, date, description).
Store expenses securely in an SQLite database.
Categorize expenses (e.g., Food, Transport, Entertainment, Bills).
Generate reports:
Monthly expense summary (total spent per month).
Category-wise spending breakdown (e.g., How much was spent on Food?).
Provide a user-friendly interface (CLI-based, with potential GUI improvements).
Ensure data integrity and error handling (handling invalid inputs, missing values, etc.).

Python Files - 
│── main.py                # Main entry point
│── db_manager.py          # Handles database setup & connection
│── expense_manager.py     # Handles adding & retrieving expenses
│── reports.py             # Generates reports (monthly & category-wise)
│── ui.py                  # CLI-based user interface
└── expense_tracker.db     # SQLite database (auto-generated)

🛠️ Features & Functionalities
1️⃣ Add Expenses
Users can enter:

Date (YYYY-MM-DD)
Amount (numeric value)
Category (Food, Transport, Entertainment, Bills, Others)
Description (optional notes)

2️⃣ View Expenses
Lists all stored expenses.
Displays data in a structured format.
3️⃣ Data Storage
Uses SQLite to store expenses persistently.
The database has a table named expenses
Allows retrieval, updates, and deletion of expenses.

4️⃣ Reports & Analysis
Monthly Expense Summary: Shows total expenses for each month.
Category-wise Expense Summary: Summarizes spending per category.
Future Enhancements: Charts and graphs for better insights.

5️⃣ Error Handling
Prevents invalid inputs (e.g., non-numeric amounts).
Ensures categories are valid.

How to Execute -
Run db_manager.py first to create the database and table.
Then run the main.py file to run the application.

Why is this Project Useful?
✔ Personal Finance Management: Helps track and analyze spending.
✔ Real-World Python Application: Uses databases, CLI interaction, and data analysis.
✔ Modular & Scalable: Can be expanded into a GUI-based or cloud-based app.
Handles database connection issues gracefully.
