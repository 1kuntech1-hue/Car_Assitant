import os
import mysql.connector
from urllib.parse import urlparse
from dotenv import load_dotenv

# Try Streamlit secrets first
try:
    import streamlit as st
    DATABASE_URL = st.secrets.get("DATABASE_URL")
except ImportError:
    DATABASE_URL = None

# Fallback to local .env
if DATABASE_URL is None:
    from dotenv import load_dotenv
    load_dotenv()
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
