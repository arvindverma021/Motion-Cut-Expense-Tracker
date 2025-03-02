import sqlite3

DB_NAME = "expense_tracker.db"


def create_db():
    """Creates the expenses table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT
    )
    """)

    conn.commit()
    conn.close()
    print("✅ Database initialized successfully!")


def check_table_exists():
    """Checks if the expenses table exists."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='expenses'")
    table = cursor.fetchone()

    conn.close()

    if table:
        print("✅ Table 'expenses' exists!")
    else:
        print("❌ Table 'expenses' is missing! Run `create_db()`.")

def get_db_connection():
    """Returns a connection to the database."""
    return sqlite3.connect(DB_NAME)

if __name__ == "__main__":
    create_db()
    check_table_exists()
