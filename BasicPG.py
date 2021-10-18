import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='bookinv' user='bookinv' password='bookinv@12345' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn=psycopg2.connect("dbname='bookinv' user='bookinv' password='bookinv@12345' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store(item, quantity, price) VALUES(%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn=psycopg2.connect("dbname='bookinv' user='bookinv' password='bookinv@12345' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

def delete(item):
    conn=psycopg2.connect("dbname='bookinv' user='bookinv' password='bookinv@12345' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item, ))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='bookinv' user='bookinv' password='bookinv@12345' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

create_table()
insert("Coffee cup", 10, 8.5)
print(view())
delete("Coffee cup")
print(view())
insert("Coffee package", 10, 8.5)
print(view())
update("Coffee package", 20, 15)
print(view())