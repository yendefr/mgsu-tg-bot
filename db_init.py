import sqlite3

def create_table_users():
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
