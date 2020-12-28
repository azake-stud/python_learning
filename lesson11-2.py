import sqlite3



conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

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


cursor.execute('SELECT * FROM users')
# one_result = cursor.fetchone()
# print(one_result)
#
# three_result = cursor.fetchmany(3)
# print(three_result)

all_result = cursor.fetchall()
#print(all_result)
print(all_result[24:])
