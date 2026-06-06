# 🏥 Medical Chatbot — AI-Powered RAG Application
---

## 🚀 Live Demo

👉 **[Try the Medical Chatbot Live](https://huggingface.co/spaces/Sg31Ghosh/medical-chatbot)**

> Ask any medical question and get accurate, context-aware answers powered by a RAG pipeline.

---

## 📌 Overview

The **Medical Chatbot** is an end-to-end AI application that leverages **Retrieval Augmented Generation (RAG)** to answer medical questions accurately using knowledge extracted from medical literature. Instead of relying solely on the LLM's training data, the chatbot retrieves relevant context from a curated medical knowledge base before generating responses — making answers more accurate, grounded, and trustworthy.

---

## 🏗️ Architecture

```
User Query
    │
    ▼
Flask Web App (app.py)
    │
    ▼
HuggingFace Embeddings          Pinecone Vector Store
(all-MiniLM-L6-v2)     ──────►  (medical knowledge base)
    │                                      │
    │                            Similarity Search (k=3)
    │                                      │
    ▼                                      ▼
OpenAI GPT-4o  ◄──────────  Retrieved Context Chunks
    │
    ▼
Final Response → User
```

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| **LLM** | OpenAI GPT-4o |
| **Embeddings** | HuggingFace `sentence-transformers/all-MiniLM-L6-v2` (384 dimensions) |
| **Vector Store** | Pinecone (cosine similarity, serverless) |
| **Framework** | LangChain 0.3.26 |
| **Backend** | Flask 3.1.1 |
| **Frontend** | HTML, CSS, JavaScript |
| **Containerization** | Docker |
| **Deployment** | Hugging Face Spaces |
| **CI/CD** | GitHub Actions + AWS ECR + AWS EC2 |

---

## ✨ Features

- 🔍 **RAG Pipeline** — Retrieves relevant medical context before generating answers
- 🧠 **GPT-4o Powered** — State-of-the-art LLM for accurate medical responses
- 💬 **Conversation Memory** — Remembers chat history within a session
- 📄 **PDF Knowledge Base** — Medical knowledge extracted and indexed from medical literature
- 🐳 **Dockerized** — Fully containerized for consistent deployment
- ⚡ **Fast Retrieval** — Pinecone vector database for millisecond similarity search
- 🎨 **Clean Chat UI** — Intuitive and responsive chat interface

---

## 📁 Project Structure

```
Medical-Chatbot/
├── src/
│   ├── helper.py          # PDF loading, text splitting, embeddings
│   └── prompts.py         # System prompt for the chatbot
├── templates/
│   └── chat.html          # Frontend chat interface
├── static/                # CSS and JS files
├── data/                  # Medical PDF knowledge base
├── research/              # Jupyter notebooks for experimentation
├── app.py                 # Main Flask application
├── vector_store_index.py  # Pinecone index creation script
├── Dockerfile             # Docker configuration
├── requirements.txt       # Python dependencies
└── .github/
    └── workflows/
        └── cicd.yaml      # CI/CD pipeline configuration
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10+
- Pinecone API Key
- OpenAI API Key

### 1. Clone the repository
```bash
git clone https://github.com/Souradeep-ghosh/Medical-Chatbot.git
cd Medical-Chatbot
```

### 2. Create and activate virtual environment
```bash
conda create -n medicalbot python=3.10
conda activate medicalbot
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```
PINECONE_API_KEY=your_pinecone_api_key
OPENAI_API_KEY=your_openai_api_key
```

### 5. Create Pinecone vector store
```bash
python vector_store_index.py
```

### 6. Run the application
```bash
python app.py
```
Visit `http://localhost:8080` in your browser.

---

## 🐳 Docker Deployment

```bash
# Build the image
docker build -t medical-chatbot .

# Run the container
docker run -p 7860:7860 \
  -e PINECONE_API_KEY=your_key \
  -e OPENAI_API_KEY=your_key \
  medical-chatbot
```

---

## 🔄 CI/CD Pipeline

The project uses **GitHub Actions** for automated deployment:

```
Push to main branch
        │
        ▼
Continuous Integration
  - Build Docker image
  - Push to Amazon ECR
        │
        ▼
Continuous Deployment
  - Pull image from ECR
  - Deploy to AWS EC2
```

---

## 🧠 How RAG Works in This Project

1. **Ingestion:** Medical PDF is loaded and split into 500-character chunks with 20-character overlap
2. **Embedding:** Each chunk is embedded using `all-MiniLM-L6-v2` (384-dimensional vectors)
3. **Indexing:** Embeddings are stored in Pinecone with cosine similarity metric
4. **Retrieval:** At query time, top-3 most similar chunks are retrieved
5. **Generation:** Retrieved context + user query are passed to GPT-4o for response generation

---

## 📦 Dependencies

```
langchain==0.3.26
langchain-community==0.3.26
langchain-pinecone==0.2.8
langchain-openai==0.3.24
langchain-huggingface
langchain-text-splitters
flask==3.1.1
sentence-transformers==4.1.0
pypdf==5.6.1
python-dotenv==1.1.0
pinecone-client
```

---

## 👨‍💻 Author

**Souradeep Ghosh**
- 📧 Connect on [LinkedIn](https://www.linkedin.com/in/souradeep-ghosh-165802150/)
- 🐙 [GitHub](https://github.com/Souradeep-ghosh)
- 🤗 [Hugging Face](https://huggingface.co/Sg31Ghosh)

---


⭐ **If you found this project helpful, please give it a star!**