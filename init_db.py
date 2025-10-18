from app.database import get_connection
from app.models import create_tables

if __name__ == "__main__":
    with get_connection() as conn:
        create_tables(conn)
        print("✅ База данных и таблицы созданы.")
