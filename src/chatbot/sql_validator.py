def validate_sql(sql):

    blocked = [
        "DROP",
        "DELETE",
        "UPDATE",
        "INSERT",
        "ALTER"
    ]

    sql_upper = sql.upper()

    for keyword in blocked:

        if keyword in sql_upper:
            return False

    return True