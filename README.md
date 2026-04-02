# 🚀 VectorGate – RAG-based AI Chatbot Backend

VectorGate is a **Retrieval-Augmented Generation (RAG) based backend system** that combines vector search and Large Language Models (LLMs) to provide accurate, context-aware answers.

It uses **FAISS for fast document retrieval** and **Google Gemini API** to generate human-like responses.

---

## 📌 Features

* 🔍 Semantic search using vector embeddings
* ⚡ Fast retrieval using FAISS vector database
* 🤖 Context-aware response generation using Gemini LLM
* 🌐 API-based interaction using FastAPI
* 💬 WebSocket support for real-time communication
* 📄 Knowledge ingestion with text chunking

---

## 🏗️ Architecture

1. **Data Ingestion**

   * Load knowledge data
   * Split into chunks using text splitter
   * Convert chunks into embeddings

2. **Vector Storage**

   * Store embeddings in FAISS for similarity search

3. **Retrieval**

   * Retrieve top relevant documents based on user query

4. **Generation**

   * Pass retrieved context + query to Gemini API
   * Generate human-like response

5. **Backend**

   * FastAPI server with WebSocket support

---

## 🛠️ Tech Stack

* **Backend:** FastAPI
* **Vector Database:** FAISS
* **Embeddings:** HuggingFace (`all-MiniLM-L6-v2`)
* **LLM:** Google Gemini API (`gemini-1.5-flash`)
* **Language:** Python

---

## 📂 Project Structure

```
vectorgate/
│── main.py              # FastAPI app with WebSocket
│── ingest.py            # Knowledge ingestion and vector creation
│── retriever.py         # Retrieves relevant documents
│── generator.py         # LLM response generation
│── data/
│   └── knowledge.py     # Input knowledge base
│── vectorstore/         # Stored FAISS index
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/your-username/vectorgate.git
cd vectorgate
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Add your API key in `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Usage

### Step 1: Ingest Knowledge

```
python ingest.py
```

### Step 2: Run Server

```
uvicorn main:app --reload
```

### Step 3: Access API

Open in browser:

```
http://127.0.0.1:8000/
```

You can test the chatbot using:

* WebSocket clients (Postman / browser tools)
* API endpoints

---

## 💡 Example Workflow

* User sends a query
* System retrieves relevant content using FAISS
* Context is passed to Gemini LLM
* LLM generates a concise, human-like answer

---

## 🚀 Future Improvements

* Add frontend interface
* Add conversation memory
* Improve summarization using LLM
* Support multiple documents/files

---

## 📊 Key Highlights

* Built complete **RAG pipeline (Retrieval + Generation)**
* Improved answer relevance using context-based retrieval
* Designed scalable backend with real-time communication

---

## 👩‍💻 Author

Lakshmi Harshitha Karlapati
