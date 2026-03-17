import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

# using when streamlt coloud--------
genai.configure(api_key=st.secrets["GoogleGemini_API_KEY"])

# using when streamlt coloud--------
# load_dotenv()

# API_KEY=os.getenv('GEMINI_API_KEY')

# genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_sql(question):

    prompt = f"""
    You are a MySQL expert.

    Table name: cars_data

    Columns:
    Model, Year, Price, Transmission, Mileage,
    FuelType, Tax, Mpg, EngineSize 

    Convert the user question into a SQL query.

    Only return SQL query.

    Question: {question}
    """

    response = model.generate_content(prompt, generation_config={"max_output_tokens":120})
    
    # Safety checks
    if not response or not hasattr(response, "text") or response.text is None:
        return ""  # fallback empty SQL

    sql = response.text.strip()

    # Remove markdown formatting
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql
