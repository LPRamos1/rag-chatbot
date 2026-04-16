# 🔎 RAG Chatbot with ChromaDB + Groq

A Python project built to learn how Retrieval-Augmented Generation (RAG) systems work by combining vector search (ChromaDB) with LLM responses (Groq API).

---

## 🚀 Features

- Store text data in a vector database (ChromaDB)
- Perform semantic search using embeddings
- Retrieve most relevant context based on user queries
- Use retrieved context to enhance LLM responses (RAG pipeline)
- Interactive terminal chatbot interface

---

## 🛠️ Tech Stack

- Python 3.11
- ChromaDB
- Groq API (LLM - Llama 3)
- dotenv (environment variables)

---

## ⚙️ How it works

The system stores a small dataset of support-related knowledge in a vector database.

When the user sends a query:

1. The query is converted into embeddings internally by ChromaDB
2. The most relevant documents are retrieved using semantic similarity
3. The retrieved context is passed to a Large Language Model (Groq API)
4. The model generates a response grounded in the retrieved context

**Pipeline:**

Input → Vector Search → Context Retrieval → LLM Generation → Response

---

## 📦 Project Structure

```bash
main.py → RAG orchestration (retrieval + chat loop)
vector_store.py → ChromaDB setup, insert, and query logic
chatbot.py → Groq API integration and streaming response
data/sample_data.py → Small knowledge base for testing
```

---

## ▶️ How to run

```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot

pip install chromadb groq python-dotenv

python main.py
```

---

## 💬 Example Interaction

You: what does blue light mean on modem
Chatbot: A flashing blue light indicates that the device is searching for a Wi-Fi connection.

You: how long does battery last
Chatbot: The battery provides approximately 12 hours of life under normal operating conditions.

---

## 🎯 Purpose

This project was built as part of my learning process in AI engineering fundamentals, focusing on:

- Vector databases and semantic search
- Retrieval-Augmented Generation (RAG) systems
- LLM integration using APIs
- Prompt engineering with context injection

It is a learning implementation of a basic RAG pipeline, not a production system.

---

## 📚 What I learned

- How RAG systems work in practice
- How vector databases retrieve semantically similar data
- How to integrate LLM APIs (Groq) with external context
- How prompt design affects LLM behavior
- Basic architecture of AI applications

---

## 🚀 Next step

his project is a foundation for future improvements such as:

- Chunking larger documents (PDF-based RAG)
- Better retrieval ranking strategies
- UI interface (Streamlit or web app)
- Using external datasets instead of small static data
