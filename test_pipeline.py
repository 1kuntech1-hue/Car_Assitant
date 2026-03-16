from ai_engine.sql_generator import generate_sql
from database.query_executor import execute_query

question = "Which car has the best fuel efficiency?"

sql = generate_sql(question)

print("Generated SQL:")
print(sql)

result = execute_query(sql)

print("Database Result:")
print(result)