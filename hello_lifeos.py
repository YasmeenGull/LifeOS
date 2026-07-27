import sqlite3
from datetime import datetime

conn = sqlite3.connect("lifeos.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS activities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    activity TEXT,
    timestamp TEXT
)
""")

activity = input("Enter Activity: ")

cursor.execute(
    "INSERT INTO activities (activity, timestamp) VALUES (?, ?)",
    (activity, str(datetime.now()))
)

conn.commit()

print("Activity Saved Successfully!")

conn.close()

