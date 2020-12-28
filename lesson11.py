import sqlite3
from data import data, orders

conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

# cursor.execute('ВАШ ЗАПРОС ТУТ')

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users(
    userid INTEGER PRIMARY KEY,
    fname TEXT,
    lname TEXT,
    gender TEXT) ;
    """)
conn.commit()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS orders(
    orderid INTEGER PRIMARY KEY,
    date TEXT,
    userid TEXT,
    total TEXT) ;
    """)
conn.commit()

cursor.execute(
    """
    INSERT INTO users(userid, fname, lname, gender)
    VALUES('00001', 'Alex', 'Smith', 'male');
    """)
conn.commit()

user = ('00002', 'Lois', 'Lane', 'female')

cursor.execute("INSERT INTO users VALUES(?,?,?,?) ;", user)
conn.commit()

more_users = [
    ('00003', 'Peter', 'Parker', 'male'),
    ('00004', 'Bruce', 'Wayne', 'male')
]

cursor.executemany(
    """
    INSERT INTO users VALUES (?,?,?,?);
    """, more_users
)
conn.commit()





cursor.executemany(
    """
    INSERT INTO users VALUES (?,?,?,?);
    """, data
)
conn.commit()

cursor.executemany(
    """
    INSERT INTO orders VALUES (?,?,?,?);
    """, orders
)
conn.commit()
conn.close()
