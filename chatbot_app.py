import streamlit as st
import google.generativeai as genai
import os

# Config
st.set_page_config(page_title="Ask Prem's Portfolio", layout="wide")
st.title("🤖 Ask Prem About His Projects")

# Load API key from environment or secrets
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

# Sample context: paste from your resume
context = """
I'm Prem Jha, a Flutter Developer with 1.5+ years' experience. 
I’ve worked on AI chat apps (DocuVerse using LangChain & Ollama), Fantasy Sports (Zoccer11 with SSE), 
E-commerce (Easyar), and Python APIs (OneTouchPost). I'm skilled in Flutter, Firebase, Python, APIs, SSE, and LangChain.
"""

# Input
user_input = st.text_input("Ask about my work, e.g., 'What did you build in Zoccer11?'")

# Chat logic
if user_input:
    with st.spinner("Thinking..."):
        response = model.generate_content(f"{context}\n\nQuestion: {user_input}")
        st.success(response.text)
