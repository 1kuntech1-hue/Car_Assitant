# if i am using local database then it work
# from config import get_connection

# conn = get_connection()
# try:
#     conn = get_connection()

#     if conn.is_connected():
#         print("✅ Database connected successfully")

# except Exception as e:
#     print("❌ Error:", e)


# now i am using railway online server...it connect with online server..
# test_db.py
from db_config import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM cars_data")

result = cursor.fetchone()

print("Total cars in database:", result[0])

cursor.close()
conn.close()