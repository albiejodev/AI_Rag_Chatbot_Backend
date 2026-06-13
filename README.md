# AI RAG Chatbot Backend

A Retrieval-Augmented Generation (RAG) backend built with FastAPI, Google Gemini, ChromaDB, and LangChain. The application allows users to upload PDF documents, store their content as vector embeddings, and interact with the documents using natural language questions.

---

## Features

* PDF Upload and Processing
* PDF Text Extraction
* Document Chunking
* Embedding Generation using Gemini Embeddings
* Vector Storage with ChromaDB
* Semantic Search
* RAG-based Question Answering
* Source Citation Support
* Document Listing
* Document Deletion
* Structured Logging
* FastAPI REST APIs

---

## Tech Stack

### Backend

* Python 3.12+
* FastAPI
* Uvicorn

### AI / RAG

* Google Gemini
* LangChain
* ChromaDB

### PDF Processing

* PyPDFLoader

### Configuration

* python-dotenv
* Pydantic

---

## Project Structure

```text
app/
│
├── api/
│   ├── upload.py
│   ├── chat.py
│   ├── search.py
│   ├── document.py
│   └── debug.py
│
├── db/
│   └── chroma_db.py
│
├── services/
│   ├── pdf_service.py
│   ├── chunk_service.py
│   ├── embedding_service.py
│   ├── gemini_service.py
│   └── rag_service.py
│
├── schemas/
│   └── chat_schema.py
│
├── logger.py
├── config.py
└── main.py

uploads/
chroma_data/
logs/
```

---

## System Architecture

```text
PDF Upload
     |
     v
PDF Parsing
     |
     v
Document Objects
     |
     v
Chunking
     |
     v
Embeddings
     |
     v
ChromaDB
     |
     v
Semantic Retrieval
     |
     v
Gemini
     |
     v
Response + Sources
```

---

## How RAG Works

### 1. Upload Document

Users upload a PDF document.

### 2. Extract Text

The PDF is parsed using LangChain's PDF loader.

### 3. Create Chunks

Large documents are split into smaller chunks using a recursive text splitter.

### 4. Generate Embeddings

Each chunk is converted into a high-dimensional vector using Gemini Embeddings.

### 5. Store in ChromaDB

Embeddings and metadata are stored inside ChromaDB.

### 6. Retrieve Relevant Chunks

When a user asks a question:

* Question is embedded
* Similar vectors are searched
* Top matching chunks are retrieved

### 7. Generate Response

Retrieved chunks are injected into a prompt and sent to Gemini.

Gemini generates an answer grounded in the uploaded documents.

---

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd AI-RAG-CHATBOT
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Environment

Windows:

```bash
env\Scripts\activate
```

Linux/Mac:

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Server

```bash
python -m uvicorn app.main:app --reload
```

---

## API Endpoints

### Upload PDF

```http
POST /upload
```

Uploads a PDF, extracts text, creates embeddings and stores chunks in ChromaDB.

---

### Chat With Documents

```http
POST /chat
```

Request:

```json
{
  "question": "What experience do I have with microservices?"
}
```

Response:

```json
{
  "answer": "You have experience designing scalable microservice architectures...",
  "sources": [
    {
      "file_name": "Resume.pdf",
      "page": 0
    }
  ]
}
```

---

### Semantic Search

```http
GET /search?query=engineering
```

Returns top matching chunks from the vector database.

---

### List Documents

```http
GET /documents
```

Returns all uploaded documents.

---

### Delete Document

```http
DELETE /documents/{document_id}
```

Deletes all vectors associated with a document.

---

### Debug

```http
GET /debug
```

Returns total stored chunks.

---

## Logging

Application logs are written to the logs directory and include:

* File Uploads
* Chunk Creation
* Embedding Generation
* Retrieval Events
* API Errors

---

## Future Improvements

### Backend

* JWT Authentication
* Multi-user Support
* Redis Caching
* Background Processing
* Streaming Responses
* Hybrid Search
* Re-ranking
* Conversation Memory
* PostgreSQL Metadata Storage

### Frontend

* React / Next.js UI
* Chat Interface
* Drag & Drop Upload
* Document Management Dashboard

### AI

* LangChain Retrieval Chains
* LangGraph Agents
* Multi-document Reasoning
* Voice Assistant Integration

---

## Learning Outcomes

This project demonstrates practical knowledge of:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embeddings
* Semantic Search
* Prompt Engineering
* LangChain
* FastAPI
* Gemini APIs
* Production Backend Design

---

## Author

Albin Joseph

Full Stack Engineer | MERN Stack Developer | AI Engineering Enthusiast
