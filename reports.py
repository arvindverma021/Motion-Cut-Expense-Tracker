import sqlite3
import pandas as pd
from db_manager import get_db_connection


def monthly_summary():
    """Displays total expenses per month."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT SUBSTR(date, 1, 7) AS month, SUM(amount) 
    FROM expenses GROUP BY month
    """)

    summary = cursor.fetchall()
    conn.close()

    print("\n📅 Monthly Expense Summary:")
    for row in summary:
        print(f"Month: {row[0]}, Total Spent: ${row[1]:.2f}")


def category_summary():
    """Displays total expenses per category."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT category, SUM(amount) 
    FROM expenses GROUP BY category
    """)

    summary = cursor.fetchall()
    conn.close()

    print("\n📊 Category-wise Expense Summary:")
    for row in summary:
        print(f"Category: {row[0]}, Total Spent: ${row[1]:.2f}")
