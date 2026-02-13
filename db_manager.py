import duckdb
from config import DB_PATH

def get_connection():
    """Establishes a connection to the persistent DuckDB file."""
    return duckdb.connect(DB_PATH)

def init_db():
    """Initializes the table schema if it doesn't exist."""
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS alpha_scores (
                ticker TEXT,
                headline TEXT,
                alpha_score FLOAT,
                sentiment TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        print(f"Database initialized successfully at: {DB_PATH}")

if __name__ == "__main__":
    init_db()