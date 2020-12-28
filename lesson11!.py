# import sqlite3
#
#
# conn = sqlite3.connect('orders.db')  # db = data base
# cursor = conn.cursor()
# cursor.execute('ВАШ ЗАПРОС ТУТ') # sql запросы пишется с большой буквы
# curser.execute(
#     """
#     CREATE TABLE IF NOT EXISTS users(
#     userid INT PRIMARY KEY UNIQUE,
#     fname TEXT,
#     lname TEXT,
#     gender TEXT) ;
#     """)
# conn.commit()
#
# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS orders(
#     orderid INT PRIMARY KEY UNIQUE,
#     date TEXT,
#     userid TEXT,
#     total TEXT) ;
#     """)
# conn.commit()
#
# cursor.execute(
#     """
#     INSERT INTO users(userid, fname, lname, gender)
#     VALUES('00001', 'Alex', 'Smith', 'male');
#     """)
# conn.commit()
#
# user = ('00002', 'Lois', 'Lane', 'female')
#
# cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?);", user)
# conn.commit()
#
# more_users = [
#     """
#     ('00003', 'Peter', 'Parker', 'male'),
#     ('00004', 'Bruce', 'Wayne', 'male')
#     """]

# import sqlite3
#
# con = sqlite3.connect("samples.db")
# cur = con.cursor()
# cur.execute(
#     """
#     CREATE TABLE IF NOT EXISTS samples(
#     first INTEGER,
#     second TEXT);
#     """)
# examples = [(2, 'def'), (3, 'ghi'), (4, 'jkl')]
# cur.executemany('INSERT INTO samples VALUES (?, ?)', examples)
# con.commit()
# for row in cur.execute('SELECT * FROM samples'):
#     print(row)
#
#
# >>>>>>>>>>>>>>>>>>>>>>>>
import sqlite3

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
    """, data
)
conn.commit()



