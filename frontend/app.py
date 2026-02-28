import streamlit as st
import requests

st.title("🚢 Titanic Chat Agent")

question = st.text_input("Ask about Titanic passengers:")

if st.button("Submit"):
    response = requests.post(
        "http://localhost:8000/ask",
        json={"question": question}
    )
    
    result = response.json()
    
    st.write(result["answer"])