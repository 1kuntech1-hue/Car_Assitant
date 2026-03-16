from database.config import get_connection


def execute_query(query):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result