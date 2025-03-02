import sqlite3
from db_manager import get_db_connection


def add_expense(date, amount, category, description):
    """Inserts an expense into the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO expenses (date, amount, category, description) 
    VALUES (?, ?, ?, ?)
    """, (date, amount, category, description))

    conn.commit()
    conn.close()
    print("Expense added successfully!")


def view_expenses():
    """Fetches all expenses from the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    conn.close()
    return expenses
