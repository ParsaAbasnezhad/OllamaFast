# 🤖 AI Chat Backend

A scalable AI chat backend built with **FastAPI**, **Ollama**, **PostgreSQL**, and **SQLAlchemy**. This project is designed with a clean, modular architecture and follows production-ready development practices.

---

## 🚀 Features

* FastAPI REST API
* Local LLM integration with Ollama
* PostgreSQL database
* SQLAlchemy 2.0 ORM
* Alembic database migrations
* Modular project architecture
* Conversation-ready database design
* Environment-based configuration
* Streaming AI responses
* Pydantic data validation
* Ready for JWT authentication
* Ready for Docker deployment

---

## 🛠 Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy 2.0
* Alembic
* Ollama
* Pydantic
* Uvicorn

---

## 📁 Project Structure

```text
app/
├── core/
├── database/
│   ├── base.py
│   ├── database.py
│   └── dependencies.py
├── models/
│   ├── user.py
│   ├── chat.py
│   └── message.py
├── routers/
├── schemas/
├── services/
├── repositories/
└── main.py

alembic/
├── versions/
└── env.py
```

---

## 🗄 Database Schema

```text
User
│
└── Chat
      │
      └── Message
```

* One User → Many Chats
* One Chat → Many Messages

---

## 📌 Current Progress

* ✅ FastAPI project initialized
* ✅ Ollama integration completed
* ✅ Streaming responses implemented
* ✅ PostgreSQL connected
* ✅ SQLAlchemy 2.0 configured
* ✅ Alembic configured
* ✅ Database migrations completed
* ✅ User model implemented
* ✅ Chat model implemented
* ✅ Message model implemented
* ✅ Entity relationships established

---

## 🔜 Upcoming Features

* JWT Authentication
* User Registration & Login
* Chat CRUD Operations
* Conversation Memory
* Chat History
* Prompt Templates
* Repository Pattern
* Service Layer
* Docker Support
* Unit & Integration Tests

---

## 📄 License

This project is intended for educational purposes and production-ready backend architecture practice.
