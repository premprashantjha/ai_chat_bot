import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

st.set_page_config(page_title="Ask Prem's Portfolio", layout="wide")

# Title
st.title("🤖 Ask Me About My Projects – Prem Jha")

# Upload resume text
loader = TextLoader("prem_resume_projects.md")
docs = loader.load()

# Split text into chunks
splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# Embed chunks
embeddings = OllamaEmbeddings(model="mistral")
vectorstore = FAISS.from_documents(chunks, embeddings)

# Create retrieval-based QA chain
retriever = vectorstore.as_retriever()
llm = Ollama(model="mistral")

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Chat Input
query = st.text_input("Ask something like: 'Tell me about Zoccer11' or 'What AI tools have you used?'")

if query:
    with st.spinner("Thinking..."):
        response = qa_chain.run(query)
        st.success(response)
