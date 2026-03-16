# db_config.py
import mysql.connector
from urllib.parse import urlparse

# Your Railway connection URL
DATABASE_URL = "mysql://root:cnYsjKmSoXmIdJNnulwJSgTVoihzkxOQ@nozomi.proxy.rlwy.net:37884/railway"

# Parse URL
parsed_url = urlparse(DATABASE_URL)

# Create a connection function
def get_connection():
    conn = mysql.connector.connect(
        user=parsed_url.username,
        password=parsed_url.password,
        host=parsed_url.hostname,
        port=parsed_url.port,
        database=parsed_url.path.lstrip('/')
    )
    return conn
    
# import mysql.connector
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def get_connection():
#     conn = mysql.connector.connect(
#         host=os.getenv("DB_HOST"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASSWORD"),
#         database=os.getenv("DB_NAME")
#     )
#     return conn



# import mysql.connector

# def get_connection():
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="1234",
#         database="car_inventory"
#     )
#     return conn
