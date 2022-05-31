import sqlite3


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_product(conn, product):
    try:
        sql = '''INSERT INTO products
                (title, price, quantity)
                VALUES(?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_product(conn, product):
    try:
        sql = '''UPDATE products SET
        price= ?, quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
    except sqlite3.Error as e:
        print(e)


def select_products_by_price_quantity_title(conn, product):
    try:
        sql = '''SELECT * FROM products WHERE price <= ? and quantity >= ? or product_title = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        rows = cursor.fetchall()
        for r in rows:
            print(r)
    except sqlite3.Error as e:
        print(e)


product_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0,
)
'''


database = r'hw_8.db'

conn = create_connection(database)

if conn is not None:
    create_table(conn, product_table)
    insert_product(conn, ('beautiful-Elina', 135.12, 64353))
    insert_product(conn, ('cool-Elina', 135.12, 64353))
    insert_product(conn, ('dear-Elina', 135.12, 64353))
    insert_product(conn, ('the-best-Elina', 135.12, 64353))
    insert_product(conn, ('smart-Elina', 135.12, 64353))
    insert_product(conn, ('mimimish-Elina', 135.12, 64353))

    select_all_products(conn)

    update_product(conn, (64353, 64456670.38, 2))

    delete_product(conn, 15)


    select_products_by_price_quantity_title(conn, (10.70, 10, 'cool-Elina'))

    conn.close()
else:
    print('ERROR! ' + database)