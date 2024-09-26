import sqlite3


connection = sqlite3.connect('ex.1.db')
cursor = connection.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        code TEXT NOT NULL PRIMARY KEY,
        title TEXT NOT NULL
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS store (
        store_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category_code TEXT NOT NULL,
        unit_price REAL DEFAULT 0.0, 
        stock_quantity INTEGER DEFAULT 0,
        store_id INTEGER,
        FOREIGN KEY (category_code) REFERENCES categories(code),
        FOREIGN KEY (store_id) REFERENCES store(store_id)
    )
''')


categories = [
    ('FD', 'Food products'),
    ('ES', 'Electronics'),
    ('CL', 'Clothes')
]
cursor.executemany('INSERT OR IGNORE  INTO categories (code, title) VALUES (?, ?)', categories)


stores = [
    ('Sheker',),
    ('Dostor',),
    ('Narodnyi',)
]
cursor.executemany('INSERT OR IGNORE INTO store (title) VALUES (?)', stores)


products = [
    ('ice-cream', 'FD', 35.0, 90, 1),
    ('samsung A41', 'ES', 15000.0, 15, 2),
    ('milk', 'FD', 575.0, 25, 1),
    ('skirt', 'CL', 500.0, 200, 3),
    ('socks', 'CL', 100.0, 200, 3),
    ('asus', 'ES', 45000.0, 23, 3 )
]
cursor.executemany('''
    INSERT OR IGNORE INTO products (title, category_code, unit_price, stock_quantity, store_id)
    VALUES (?, ?, ?, ?, ?)
''', products)

connection.commit()


print('ДОБРО ПОЖАЛОВАТЬ В СЕТЬ МАГАЗИНОВ! Вы можете отобразить список продуктов по выбранному id магазина.')
print('1. Sheker \n2. Dostor \n3. Narodnyi')

listmag = None
while listmag != 0:
    try:
        listmag = int(input("ПОЖАЛУЙСТА введите id магазина или 0 для выхода: "))

        if listmag in [1, 2, 3]:
            cursor.execute('''
                SELECT products.title, categories.title, products.unit_price, products.stock_quantity
                FROM products
                JOIN categories ON products.category_code = categories.code
                WHERE products.store_id = ?
            ''', (listmag,))
            products_in_store = cursor.fetchall()

            if products_in_store:
                for product in products_in_store:
                    print(f"Название продукта: {product[0]}")
                    print(f"Категория: {product[1]}")
                    print(f"Цена: {product[2]}")
                    print(f"Количество на складе: {product[3]}")
                    print('-' * 30)
            else:
                print("Продукты в ЭТОМ магазине не найдены.")
        elif listmag == 0:
            print("Выход из программы.")
            break
        else:
            print("Неверный id магазина. Попробуйте ЕЩЕ раз.")
    except ValueError:
        print("Пожалуйста, введите корректное число!")


connection.close()

