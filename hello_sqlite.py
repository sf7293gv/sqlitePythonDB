import sqlite3

db ='first_db.sqlite'

def create_table():
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE products (id int, name text)')
    conn.close()

def insert_example_data():
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products values (1000, "hat")')
        conn.execute('INSERT INTO products values (1001, "shirt")')
    conn.close()

def display_all_data():
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM products')
    for row in results:
        print(row)
    conn.close()

def display_one_product(product):
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM products WHERE name like "jacket"')
    first_row = results.fetchone()
    if first_row:
        print(first_row)
    else:
        print('Not found')

def create_new_product(product):
    new_id = int(input('Enter ID: '))
    name = input('Enter product name: ')

    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products VALUES (?, ?)', (new_id, name))
    conn.close()

def update_product():
    update_product = 'wool hat'
    update_id = 1000
    
    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE products SET name = ? WHERE id = ? ', (update_product, update_id))
    conn.close()


def delete_product(product_name):
    with sqlite3.connect(db) as conn:
        conn.execute('DELETE FROM products WHERE name = ?', (product_name,))
    conn.close()

create_table()
insert_example_data()
display_all_data()
display_one_product('jacket')
create_new_product('coat')
update_product()
delete_product('jacket')

display_all_data()