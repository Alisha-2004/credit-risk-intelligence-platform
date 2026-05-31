from nl_to_sql import generate_sql
from sql_validator import validate_sql
from sql_runner import run_query

question = input(
    "Ask your question: "
)

sql = generate_sql(question)

print("\nGenerated SQL:")
print(sql)

if validate_sql(sql):

    result = run_query(sql)

    print("\nResult:")
    print(result)

else:

    print("Unsafe SQL blocked.")