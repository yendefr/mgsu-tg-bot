import sqlite3


conn = sqlite3.connect('users.db')
cursor = conn.cursor()

query = '''CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                name TEXT,
                surname TEXT,
                group_number INTEGER);'''
cursor.execute(query)

conn.commit()
cursor.close()
conn.close()
