# PDF QA Backend

This is the backend service for the PDF Question-Answering system using FastAPI and Llama 2.

## Prerequisites

1. Install Ollama from https://ollama.ai
2. Pull the Llama 2 model:
   ```bash
   ollama pull llama2
   ```

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create required directories:
   ```bash
   mkdir temp vector_db
   ```

## Running the Server

```bash
python main.py
```

The server will start at http://localhost:8000