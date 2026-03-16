from config import get_connection

conn = get_connection()
try:
    conn = get_connection()

    if conn.is_connected():
        print("✅ Database connected successfully")

except Exception as e:
    print("❌ Error:", e)

