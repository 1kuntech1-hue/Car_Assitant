import streamlit as st
from ai_engine.sql_generator import generate_sql
from database.query_executor import execute_query
from ai_engine.response_builder import build_response

st.title("🚗 Car AI Assistant")

question = st.chat_input("Ask something about cars...")

if question:
    st.write("User:", question)

    # Step 1: Generate SQL
    sql = generate_sql(question)
    
    # Step 2: Execute query
    db_result = execute_query(sql)

    # Step 3: Convert to human response
    final_response = build_response(question, db_result)

    # Step 4: Show answer
    st.write("Assistant:", final_response)