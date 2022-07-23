import sqlite3

# conn = sqlite3.connect(':memory:') //Cria um banco de dados em mamória

conn = sqlite3.connect('custumer.sqlite')

c = conn.cursor()

c.execute("""CREATE TABLE if not exists costumers (
    first_name text, 
    last_name text,
    email text
)
""")

many_costumers = [
    ('nome1', 'sobrenome1', 'email1'), 
    ('nome2', 'sobrenome2', 'email2'), 
    ('nome3', 'sobrenome3', 'email3'), 
    ('nome4', 'sobrenome4', 'email4'), 
    ('nome5', 'sobrenome5', 'email5'),
]

# c.execute("INSERT INTO costumers VALUES ('João1', 'Vitor', 'eu@gmail.com')")
c.executemany("INSERT INTO costumers VALUES (?,?,?)", many_costumers)

conn.commit()

conn.close()
