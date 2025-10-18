from .database import get_connection

def add_client(name, phone):
    with get_connection() as conn:
        conn.execute("INSERT INTO clients (name, phone) VALUES (?, ?)", (name, phone))
        conn.commit()

def list_clients():
    with get_connection() as conn:
        return conn.execute("SELECT id, name, phone FROM clients").fetchall()

def add_part(name, price):
    with get_connection() as conn:
        conn.execute("INSERT INTO parts (name, price) VALUES (?, ?)", (name, price))
        conn.commit()

def list_parts():
    with get_connection() as conn:
        return conn.execute("SELECT id, name, price FROM parts").fetchall()

def add_order(client_id, description, cost):
    with get_connection() as conn:
        conn.execute("""
        INSERT INTO orders (client_id, description, cost)
        VALUES (?, ?, ?)
        """, (client_id, description, cost))
        conn.commit()

def list_orders(limit=20):
    with get_connection() as conn:
        return conn.execute("""
        SELECT o.id, c.name, o.description, o.status, o.cost, o.date_created
        FROM orders o
        LEFT JOIN clients c ON o.client_id = c.id
        ORDER BY o.date_created DESC
        LIMIT ?
        """, (limit,)).fetchall()
