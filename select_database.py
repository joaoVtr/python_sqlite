import sqlite3

conn = sqlite3.connect('custumer.sqlite')

c = conn.cursor()

c.execute('SELECT * FROM costumers')

# print(c.fetchone())
# print(c.fetchmany(3))
print(c.fetchall())


conn.commit()

conn.close()
