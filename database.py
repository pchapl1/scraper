import sqlite3
from sqlite3 import Error

con = sqlite3.connect('scrapeymcscraperton.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE if not exists questions
               (question, author, date, tag)''')
con.close()