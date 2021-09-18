import sqlite3

# connect or create new
with sqlite3.connect('first_db.sqlite') as conn:
    # conn.execute('CREATE TABLE products (id int, name text)')
    # conn.execute('INSERT INTO products values (1000, "hat")')
    # conn.execute('INSERT INTO products values (1001, "shirt")')

    results = conn.execute('SELECT * FROM products')

    for row in results:
        print(row)

    results = conn.execute('SELECT * FROM products WHERE name like "jacket"')
    first_row = results.fetchone()
    print(first_row)

    new_id = int(input('enter new id: '))
    new_name = input('Enter new product: ')

    conn.execute('INSERT INTO products VALUES (?, ?)', (new_id, new_name))

    updated_product = 'wool hat'
    update_id = 1000
    conn.execute('UPDATE products SET name = ? WHERE id = ? ', (updated_product, update_id))

    delte_product = 'jacket'
    conn.execute('DELETE FROM products WHERE name = ?', (delte_product,))
conn.close() 

create_table()

insert_example_data()

display_all_data()

