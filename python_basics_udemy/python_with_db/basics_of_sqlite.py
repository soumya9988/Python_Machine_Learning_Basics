import sqlite3


def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute(" CREATE TABLE IF NOT EXISTS store ( item TEXT, quantity INTEGER, price REAL )")
    conn.commit()
    conn.close()


def insert_table(item, qty, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute(" INSERT INTO store VALUES (?, ?, ?)", (item, qty, price))
    conn.commit()
    conn.close()


def view_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_table(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = ?", (item,))
    conn.commit()
    conn.close()


def update_table(qty, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?", (qty, price, item))
    conn.commit()
    conn.close()


insert_table("Water", 5, 1.99)
insert_table('Coffee', 3, 0.99)
delete_table('Water')
update_table(1, 2.14, 'Coffee')
print(view_table())