import sqlite3
from sqlite3 import Error


def conn_to_db_and_create_table():
    con = sqlite3.connect('scrapeymcscraperton.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE if not exists questions
               (question, author, date, tag)''')
    con.close()

conn_to_db_and_create_table()