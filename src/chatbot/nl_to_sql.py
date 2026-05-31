from groq import Groq
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

schema_path = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "schema.txt"
)

with open(schema_path, "r", encoding="utf-8") as f:
    SCHEMA = f.read()


def generate_sql(question):

    prompt = f"""
You are a banking data analyst.

Database Schema:

{SCHEMA}

Rules:
1. Generate ONLY SQLite SQL.
2. Use ONLY the applications table.
3. Never use DROP.
4. Never use DELETE.
5. Never use UPDATE.
6. Never use INSERT.
7. Return ONLY SQL.
8. Do NOT use markdown.
9. Do NOT use ```sql.
10. Do NOT explain the query.

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    sql = response.choices[0].message.content.strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql