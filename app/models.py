def create_tables(conn):
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS parts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        description TEXT,
        status TEXT DEFAULT 'в работе',
        cost REAL,
        date_created TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (client_id) REFERENCES clients (id)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS order_parts (
        order_id INTEGER,
        part_id INTEGER,
        quantity INTEGER DEFAULT 1,
        FOREIGN KEY (order_id) REFERENCES orders (id),
        FOREIGN KEY (part_id) REFERENCES parts (id)
    )
    """)

    conn.commit()
