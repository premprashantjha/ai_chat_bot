# 🤖 Prem Prashant Jha – Gemini AI Chatbot Portfolio

This is an AI-powered portfolio chatbot built using **Streamlit + Gemini API** with support for **real-time Google search via SerpAPI**. It answers questions about **Prem Prashant Jha’s work, resume, and projects**, and provides a conversational experience like ChatGPT.

---

## 🚀 Features

- ✅ Conversational Chat UI (`st.chat_input()`)
- ✅ Gemini 1.5 Flash LLM integration
- ✅ Real-time Google Search using SerpAPI
- ✅ Chat memory via session state
- ✅ Context loaded from your own resume file (`premprashantjha.md`)
- ✅ Reset button to restart conversation
- ✅ Fully embeddable inside any Flutter Web portfolio

---

## 🛠 Technologies Used

- [Streamlit](https://streamlit.io/)
- [Gemini API (Google Generative AI)](https://ai.google.dev/)
- [SerpAPI](https://serpapi.com/) for Google Search
- Python, Markdown, OpenAI-style prompt formatting

---

## 📦 Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/prem-gemini-chatbot.git
cd prem-gemini-chatbot
```

2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create .streamlit/secrets.toml
```bash
GEMINI_API_KEY = "your-gemini-key"
SERPAPI_KEY = "your-serpapi-key"
```

5. Add your context file

Create a premprashantjha.md file with your resume or project details.

Hosting on Streamlit Cloud

    Push the repo to GitHub

    Go to streamlit.io/cloud

    Select the repo and choose chatbot_app.py

    Add the secrets under App Settings → Secrets

    Done!


