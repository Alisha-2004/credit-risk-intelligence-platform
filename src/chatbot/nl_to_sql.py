from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_sql(question):

    prompt = f"""
You are an expert banking SQL analyst.

Table:
applications

Generate ONLY SQLite SQL.

Rules:
- Use only SELECT queries
- Never use DROP
- Never use DELETE
- Never use UPDATE
- Never use INSERT

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()