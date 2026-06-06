import streamlit as st

from app.ai.classifier import classify_ticket

st.title("AI Service Management System")

ticket = st.text_area("Describe your issue")

if st.button("Submit Ticket"):

    result = classify_ticket(ticket)

    st.json(result)