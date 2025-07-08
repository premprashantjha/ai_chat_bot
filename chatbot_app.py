import streamlit as st
import google.generativeai as genai
import time
import os
import requests

# ---------- Streamlit Config ----------
st.set_page_config(page_title="Ask Prem Prashant Jha", layout="wide")
st.title("🤖 Ask Prem About His Work, Projects & Tech Stack")

# ---------- Load API Keys ----------
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("❌ Gemini API key is missing. Add it in Streamlit Secrets.")
    st.stop()

# ---------- Load Resume Context ----------
def load_context_from_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

context = load_context_from_file("premprashantjha.md")

# ---------- Gemini Model ----------
model = genai.GenerativeModel("gemini-1.5-flash")

# ---------- Google Search via SerpAPI (cached) ----------
@st.cache_data(show_spinner=False)
def get_top_3_links(query="Prem Prashant Jha"):
    api_key = st.secrets["SERPAPI_KEY"]
    params = {
        "q": query,
        "api_key": api_key,
        "num": 5,
        "engine": "google",
    }
    response = requests.get("https://serpapi.com/search", params=params)
    results = response.json().get("organic_results", [])

    filtered = []
    for r in results:
        link = r.get("link", "")
        if any(domain in link for domain in ["linkedin.com", "instagram.com", "bookmyshow.com"]):
            filtered.append({
                "title": r.get("title", ""),
                "snippet": r.get("snippet", ""),
                "link": link
            })
        if len(filtered) >= 3:
            break

    return filtered

def format_for_gemini(links_data):
    formatted = "Below are top online profiles about Prem Prashant Jha:\n\n"
    for i, item in enumerate(links_data, 1):
        formatted += f"🔗 Profile {i}: {item['title']}\n{item['snippet']}\nURL: {item['link']}\n\n"
    formatted += "Please provide a detailed professional + personal overview based on these."
    return formatted

# ---------- Chat State ----------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------- Reset Button ----------
if st.button("🔁 Reset Chat"):
    st.session_state.chat_history = []
    st.rerun()

# ---------- Input UI ----------
user_input = st.chat_input("💬 Ask me anything about Prem Prashant Jha...")

# ---------- Handle Chat ----------
if user_input:
    time.sleep(1)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Special Case: Real Google Search for this exact question
    if "who is prem prashant jha" in user_input.lower():
        with st.spinner("🔍 Fetching online profiles..."):
            top_links = get_top_3_links()
            if not top_links:
                reply = "❌ Could not find relevant profiles online."
            else:
                prompt_to_gemini = format_for_gemini(top_links)
                try:
                    response = model.generate_content(prompt_to_gemini)
                    reply = response.text.strip()
                except Exception as e:
                    reply = f"❌ Gemini Error: {e}"
    else:
        # Standard conversation with memory + context
        full_prompt = context + "\n\n"
        for msg in st.session_state.chat_history:
            full_prompt += f"{msg['role'].capitalize()}: {msg['content']}\n"
        try:
            response = model.generate_content(full_prompt)
            reply = response.text.strip()
        except Exception as e:
            reply = f"❌ Gemini Error: {e}"

    st.session_state.chat_history.append({"role": "assistant", "content": reply})

# ---------- Display Chat UI ----------
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        with st.chat_message("user", avatar="👤"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(msg["content"])
