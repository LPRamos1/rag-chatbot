# 🔎 RAG Chatbot with ChromaDB + Groq

A Python project exploring Retrieval-Augmented Generation (RAG) by combining vector search with LLM-based response generation.

This project focuses on building a simple but modular RAG pipeline, separating retrieval, context construction, and generation.

---

## 🚀 Features

- Semantic search using ChromaDB
- Context retrieval based on similarity search
- Prompt construction with context injection
- Streaming responses using Groq API (Llama 3)
- Modular architecture (retrieval vs generation)

---

## 🛠️ Tech Stack

- Python 3.11
- ChromaDB
- Groq API (LLM - Llama 3)
- python-dotenv

---

## ⚙️ System Design

The system follows a basic RAG pipeline:

User Query
→ Vector Search (ChromaDB)
→ Top-K Retrieval
→ Context Aggregation
→ LLM Prompt Injection
→ Response Generation

Design choices
Uses top-k retrieval (k=3) to balance relevance and context size
Context is concatenated into a single prompt block for simplicity
System prompt enforces grounded answers (no hallucination)

**Pipeline:**

Input → Vector Search → Context Retrieval → LLM Generation → Response

---

## 📦 Project Structure

- main.py # Orchestrates RAG pipeline and CLI loop
- vector_store.py # ChromaDB setup and retrieval logic
- chatbot.py # LLM API integration (streaming)
- data/ # Sample dataset

---

## ▶️ How to run

```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot

pip install -r requirements.txt

python main.py
```

---

## 💬 Example Interaction

You: how long does battery last
Chatbot: The battery provides approximately 12 hours of life under normal operating conditions.

---

## 🎯 Purpose

This is a learning-oriented implementation of a RAG system, focused on understanding

- How retrieval impacts LLM responses
- How to structure prompts with external context
- Basic architecture of AI applications

---

## 📚 Key Learnings

- Practical implementation of RAG pipelines
- Trade-offs in context size vs relevance
- Integration of vector search with LLM APIs
- How prompt design affects LLM behavior
- Prompt design for grounded responses

---

## 🚧 Limitations

- Uses a small static dataset
- No chunking or document ingestion pipeline
- No ranking optimization beyond similarity search
- CLI interface only


## 🚀 Next step

- CAdd document chunking (PDF / larger datasets)
- Improve retrieval strategies
- Add simple web interface
- External data ingestion pipeline
