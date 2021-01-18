import sqlite3

conn = sqlite3.connect("crud.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS course (courseid INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL, studyarea TEXT NOT NULL)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS student (studentid INTEGER PRIMARY KEY AUTOINCREMENT,
courseid INTEGER NOT NULL, name TEXT NOT NULL, created NUMERIC NOT NULL, age INTEGER NOT NULL,
cpf TEXT NOT NULL)""")

conn.close()