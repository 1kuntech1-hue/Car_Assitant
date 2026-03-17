import google.generativeai as genai
import streamlit as st
# import os
# from dotenv import load_dotenv

# load_dotenv()

# API_KEY=os.getenv('GEMINI_API_KEY')

# genai.configure(api_key=API_KEY)
# Correct usage
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

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

    response = model.generate_content(prompt)
    
    sql = response.text.strip()

    # Remove markdown formatting
    sql = sql.replace("```sql", "").replace("```", "").strip()

    return sql
