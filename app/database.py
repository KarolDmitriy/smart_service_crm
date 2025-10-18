import sqlite3
from pathlib import Path

DB_PATH = Path("data/smart_service.db")

def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)
