from distutils.util import execute
from os import close
import sqlite3

def connection():
    conn = sqlite3.connect('costumer.sqlite')

    return conn


def createTable():
    conn = connection()
    c = conn
    
    c.execute("""CREATE TABLE if not exists costumers (
    first_name text, 
    last_name text,
    email text
    )
    """)

    conn.commit()
    conn.close()

def showAll():
    conn = connection()

    c = conn.cursor()

    c.execute("SELECT rowid,* FROM costumers")

    items = c.fetchall() 

    for item in items:
        print(item)
    
    conn.commit()

    conn.close()

def addOne(first, last, email):
    conn= connection()

    c = conn.cursor()

    c.execute("INSERT INTO costumers VALUES (?,?,?)", (first, last, email))

    conn.commit()
    conn.close()
