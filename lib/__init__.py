import sqlite3

# Create a connection to an in-memory SQLite database
CONN = sqlite3.connect('company.db')

# Create a cursor object to interact with the database
CURSOR = CONN.cursor()
