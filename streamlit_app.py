import streamlit as st

st.title("AI Service Desk")

title = st.text_input("Title")
description = st.text_area("Description")

if st.button("Submit"):
    st.success("Ticket Created")