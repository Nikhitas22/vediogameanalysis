import sqlite3
import pandas as pd

# Connect to your database
conn = sqlite3.connect("vediogames.db")
cursor = conn.cursor()

# List all tables
print("📋 All tables in database:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for table in tables:
    print(" -", table[0])

# Show row counts
print("\n🔢 Row counts:")
for table_name in ['games', 'vgsales', 'merged_data']:
    result = cursor.execute(f"SELECT COUNT(*) FROM {table_name};").fetchone()
    print(f"{table_name}: {result[0]} rows")

# Preview top 5 rows
print("\n🔍 Sample data:")
for table_name in ['games', 'vgsales', 'merged_data']:
    print(f"\n--- {table_name.upper()} ---")
    df = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 5;", conn)
    print(df)

conn.close()