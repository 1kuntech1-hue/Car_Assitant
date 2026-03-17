from database.db_config import get_connection


def execute_query(query):
    if not query or not isinstance(query, str):
        print("Warning: empty or invalid SQL query")
        return []
        
    conn = get_connection()
    cursor = conn.cursor()

    print("Generated SQL:", query)
    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

