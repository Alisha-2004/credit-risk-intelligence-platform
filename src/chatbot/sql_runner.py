import sqlite3
import pandas as pd
from pathlib import Path

def run_sql(query):

    db_path = (
        Path(__file__).resolve().parents[2]
        / "data"
        / "credit_risk.db"
    )

    conn = sqlite3.connect(db_path)

    result = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return result