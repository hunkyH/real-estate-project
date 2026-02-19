import sqlite3
from pathlib import Path

# project_root/data/realestate.db
DB_PATH = Path(__file__).resolve().parents[1] / "data" / "realestate.db"

def get_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
