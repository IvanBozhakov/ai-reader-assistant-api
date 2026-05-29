# 📚 AI Reader Assistant API

Simple FastAPI backend that allows you to upload documents and ask questions about their content using AI.

---

# 🚀 Features

- 📄 Upload documents (PDF, TXT, DOCX)
- 🧠 Split documents into chunks
- 🔎 Semantic search using embeddings + Qdrant
- 💬 AI-powered chat responses using OpenAI

---
## Examples

## Run Server
```bash

docker compose up -d

uvicorn app.main:app --reload

```
## Upload file
```bash

curl -X POST http://127.0.0.1:8000/upload \
  -F "file=@sample.pdf"
```

## Ask for assistance
```bash

curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "What is this document about?"}'
```