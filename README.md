# PDF Question-Answering System

An interactive system that allows users to upload PDFs and ask questions about their content, receiving accurate answers with proper citations. Built with React.js, FastAPI, and advanced language models.

[PDF QA System Demo](https://youtu.be/wCb_qdF9oRo)

## 🌟 Features

- **PDF Upload & Processing**
  - Support for multiple PDF uploads (20-30 pages each)
  - Efficient text extraction and embedding generation
  - Secure file handling and storage

- **Interactive Chat Interface**
  - Real-time question-answering
  - Chat history preservation
  - Clean, modern UI with dark mode support

- **Smart Answer Generation**
  - Context-aware responses
  - Source citations with page numbers
  - Retrieval-Augmented Generation (RAG) pipeline

- **Vector Database Integration**
  - Efficient text embedding storage
  - Fast similarity search
  - Scalable document management

## 🛠️ Tech Stack

- **Frontend**
  - React 18
  - Tailwind CSS
  - shadcn/ui components

- **Backend**
  - FastAPI
  - Python 3.8+
  - LangChain
  - PyPDF for text extraction

- **Database & ML**
  - Vector Database (ChromaDB)
  - Language Model Integration (LLAMA 2)
  - Text Embeddings Pipeline

## 📋 Prerequisites

- Python 3.8 or later
- pip (Python package manager)
- Git

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/admiralpunk/RAG-Question-Answering-system.git
   cd RAG-Question-Answering-system
   ```

2. **Install Frontend Dependencies**
   ```bash
   cd frontend
   npm install
   ```

3. **Install Backend Dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables**
   ```bash
   # Create .env file in root directory
   cp .env.example .env
   # Add your configuration values
   ```

5. **Start the Development Servers**
   ```bash
   # Terminal 1: Frontend
   cd frontend
   npm run dev

   # Terminal 2: Backend
   cd backend
   uvicorn main:app --reload
   ```

6. Open [http://localhost:3000](http://localhost:3000) in your browser

## 🏗️ Project Structure

```
RAG-Question-Answering-system/
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── utils.py
│   └── requirements.txt
├── frontend/
│   ├── components/
│   │   ├── Header.js
│   │   ├── Footer.js
│   │   └── ChatInterface.js
│   ├── pages/
│   │   ├── index.js
│   │   └── _app.js
│   ├── public/
│   │   ├── styles.css
│   │   └── logo.png
│   └── package.json
└── README.md

```

## 🔧 Configuration

The system can be configured through environment variables:

```env
# Frontend
VITE_API_BASE_URL=http://localhost:8000/api

# Backend
BASE_URL=http://localhost:11434
MODEL_NAME=llama2

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



