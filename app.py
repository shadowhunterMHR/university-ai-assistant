# app.py
import streamlit as st
import os
from nlp.pipeline import run_pipeline
from llm.generator import generate_answer

# Get Hugging Face API token from environment
API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")
if not API_TOKEN:
    st.error("Hugging Face API token not found. Please set HUGGINGFACE_API_TOKEN.")
    st.stop()

# Streamlit App
st.set_page_config(page_title="University AI Assistant", page_icon="🎓", layout="centered")
st.title("🎓 University AI Assistant")
st.write("Ask anything about Riphah International University!")

# User input
user_query = st.text_input("Enter your question:", "")

if user_query:
    with st.spinner("Processing your question..."):
        # Run NLP pipeline
        nlp_result = run_pipeline(user_query)

        # Generate answer using LLM
        answer = generate_answer(
            query=user_query,
            intent=nlp_result["intent"],
            entities=nlp_result["entities"],
            documents=nlp_result["documents"],
            api_token=API_TOKEN
        )
    st.subheader("Answer:")
    st.write(answer)
