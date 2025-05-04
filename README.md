# Web Content Q&A Tool

This project is a **Retrieval-Augmented Generation (RAG) based Question Answering system** built using [LangChain](https://python.langchain.com/), [Streamlit](https://streamlit.io/), and [HuggingFace Inference API](https://huggingface.co/inference-api).  
It allows you to ingest web content from multiple URLs, embed the content, and then ask questions about it using a large language model.

---

## Features

- **Multi-URL Web Scraping:** Ingest content from one or more URLs (input one per line).
- **Text Chunking & Embedding:** Content is chunked and embedded using transformer-based models.
- **Vector Store (FAISS):** Stores embeddings locally for efficient retrieval.
- **Question Answering:** Ask free-form questions; answers are generated using a powerful LLM with retrieved context.
- **Streamlit UI:** Simple web interface for easy use.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/qna-bot.git
cd qna-bot
```

### 2. Create and Activate a Virtual Environment (Recommended)

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

## Usage

### 1. Start the Streamlit App

```bash
streamlit run app.py
```

### 2. Using the App

- **Input URLs:** Enter one or more URLs (one per line) in the text area.
- **Ingest:** Click "Ingest URL Content" to scrape and embed the content.
- **Ask Questions:** Enter your question in the question box and click "Get Answer."
- **View Answer:** The answer will appear below if relevant content is found.

---

## Project Structure

```
.
├── app.py               # Streamlit web UI
├── chunk_embed.py       # Logic for chunking and embedding web content
├── rag.py               # RAG logic: loading vector store, retrieval, answer generation
├── scraper.py           # Web scraping logic
├── logger.py            # Logging utility (add as needed)
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

---
