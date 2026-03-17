import streamlit as st
from ai_engine.sql_generator import generate_sql
from database.query_executor import execute_query
from ai_engine.response_builder import build_response

st.title("🚗 Car AI Assistant")

# ---------- SESSION STATE ----------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "last_question" not in st.session_state:
    st.session_state.last_question = None

# ---------- CHAT INPUT ----------
question = st.chat_input("Ask something about cars...")

# ---------- PROCESS ONLY NEW INPUT ----------
if question and question != st.session_state.last_question:
    # Show user message
    st.session_state.chat_history.append(("User", question))

    # Step 1: Generate SQL
    sql = generate_sql(question)
    
    # Step 2: Execute query
    db_result = execute_query(sql)

    # ---------------- Validation ----------------
    if db_result is None:
        db_result = []  # fallback to empty list to avoid TypeError
        
    # Step 3: Convert to human response
    final_response = build_response(question, db_result)
    if not isinstance(final_response, str):
        final_response = "Sorry, I could not generate a response."

    # Store assistant response
    st.session_state.chat_history.append(("Assistant", final_response))

# ---------- DISPLAY CHAT ----------
for role, msg in st.session_state.chat_history:
    st.write(f"**{role}:** {msg}")