# 🤖 AI Chat Backend

A production-style AI chat backend built with **FastAPI**, **Ollama**, **PostgreSQL**, and **SQLAlchemy 2.0**. The project follows a clean layered architecture using the **Repository Pattern** and **Service Layer**, providing persistent conversation memory powered by a local Large Language Model (LLM).

---

# 🚀 Features

- ⚡ FastAPI REST API
- 🧠 Local AI integration with Ollama
- 💬 Persistent conversation memory
- 🗄 PostgreSQL database
- 🔥 SQLAlchemy 2.0 ORM
- 📦 Alembic database migrations
- 🏗 Clean Layered Architecture
- 📂 Repository Pattern
- ⚙️ Service Layer
- ✅ Pydantic validation
- 🌱 Environment-based configuration
- 📜 Chat history support
- 🧩 Modular project structure
- 🚀 Production-ready project architecture

---

# 🛠 Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy 2.0
- Alembic
- Ollama
- Pydantic
- Uvicorn
- python-dotenv

---

# 📁 Project Structure

```text
app/
│
├── core/
├── database/
│   ├── base.py
│   ├── database.py
│   └── dependencies.py
│
├── models/
│   ├── user.py
│   ├── chat.py
│   └── message.py
│
├── repositories/
│   ├── chat_repository.py
│   └── message_repository.py
│
├── services/
│   ├── chat_service.py
│   ├── message_service.py
│   └── ollama_service.py
│
├── routers/
│   ├── chat_router.py
│   └── message_router.py
│
├── schemas/
│
└── main.py

alembic/
└── versions/
```

---

# 🗄 Database Schema

```text
User
 │
 └────────────┐
              │
            Chat
              │
              │
        ┌─────┴─────┐
        │           │
    Message     Message
        │
    (user)
        │
    (assistant)
```

Relationships

- One User → Many Chats
- One Chat → Many Messages

---

# 🔄 Chat Flow

```text
Client
   │
   ▼
FastAPI Router
   │
   ▼
Chat Service
   │
   ├── Save User Message
   │
   ├── Load Conversation History
   │
   ├── Format Messages
   │
   ├── Send to Ollama
   │
   ├── Save AI Response
   │
   ▼
PostgreSQL
```

---

# 📌 Current Progress

- ✅ FastAPI project initialized
- ✅ PostgreSQL integration
- ✅ SQLAlchemy 2.0 ORM
- ✅ Alembic migrations
- ✅ User model
- ✅ Chat model
- ✅ Message model
- ✅ Entity relationships
- ✅ Repository Pattern
- ✅ Service Layer
- ✅ Ollama integration
- ✅ Create chat endpoint
- ✅ Create message endpoint
- ✅ Retrieve conversation history
- ✅ Persistent conversation memory
- ✅ AI response persistence
- ✅ Context-aware conversations

---

# 🔜 Roadmap

- 🔐 JWT Authentication
- 👤 User Registration & Login
- 🔑 Authorization
- 🌊 Streaming Responses
- 📄 Prompt Templates
- 🧠 RAG (Retrieval-Augmented Generation)
- 📎 File Upload
- 🌐 WebSocket Chat
- 🐳 Docker & Docker Compose
- ☁️ Deployment
- 🧪 Unit Tests
- 🔍 Integration Tests

---

# 📄 License

This project is built for learning modern backend architecture, AI application development, and production-ready FastAPI practices.