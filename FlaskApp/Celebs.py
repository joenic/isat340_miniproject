import sqlite3

conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
conn.close()
