import app.models

from fastapi import FastAPI
from app.routers.chat_router import router as chat_router
from app.routers.message_router import router as message_router



app = FastAPI(
    title="AI Chat API",
    version="1.0.0"
)

app.include_router(chat_router)
app.include_router(message_router)

@app.get("/")
def root():
    return {
        "message": "FastAPI + Ollama"
    }