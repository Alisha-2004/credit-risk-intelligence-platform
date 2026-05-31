import sqlite3
import pandas as pd

def run_query(sql):

    conn = sqlite3.connect(
        "data/credit_risk.db"
    )

    result = pd.read_sql(
        sql,
        conn
    )

    conn.close()

    return result