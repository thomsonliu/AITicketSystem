import streamlit as st
import pandas as pd
import sqlite3

from app.ai.classifier import classify_ticket

st.title("AI Service Management System")

# Create database/table if it doesn't exist
conn = sqlite3.connect("tickets.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    category TEXT,
    priority TEXT,
    team TEXT
)
""")

conn.commit()
conn.close()

ticket_text = st.text_area("Describe your issue")

if st.button("Submit Ticket"):

    result = classify_ticket(ticket_text)

    st.write("AI Classification")
    st.json(result)

    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tickets (
        description,
        category,
        priority,
        team
    )
    VALUES (?, ?, ?, ?)
    """, (
        ticket_text,
        result["category"],
        result["priority"],
        result["team"]
    ))

    conn.commit()
    conn.close()

    st.success("Ticket saved successfully!")

conn = sqlite3.connect("tickets.db")

df = pd.read_sql("SELECT * FROM tickets", conn)

st.subheader("All Tickets")
st.dataframe(df)

conn.close()