from nl_to_sql import generate_sql
from sql_runner import run_sql
from response_generator import generate_response

def ask(question):

    sql = generate_sql(question)

    result = run_sql(sql)

    answer = generate_response(
        question,
        result.to_string(index=False)
    )

    print("\nGenerated SQL:")
    print(sql)

    return answer