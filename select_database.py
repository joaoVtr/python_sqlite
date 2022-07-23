import sqlite3

conn = sqlite3.connect('custumer.sqlite')

c = conn.cursor()

c.execute('SELECT * FROM costumers')

# print(c.fetchone())
# print(c.fetchone()[1])
# print(c.fetchmany(3))
# print(c.fetchmany(3)[2])

items = c.fetchall()

for item in items:
    print(item[0] + '\t' + item[1] +'\t' + item[2])

conn.commit()

conn.close()
