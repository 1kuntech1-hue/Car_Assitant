import os
import mysql.connector
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()

# our Railway connection URL
DATABASE_URL = os.getenv("DATABASE_URL")

parsed_url = urlparse(DATABASE_URL)



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