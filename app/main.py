from fastapi import FastAPI
from app.routers.chat import router

app = FastAPI(
    title="AI Chat API",
    version="1.0.0"
)
app.include_router(router)
@app.get("/")
def root():
    return {
        "message": "FastAPI + Ollama"
    }

from sqlalchemy import text
from app.database.database import engine

@app.get("/db-test")
def db_test():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        return {"result": result.scalar()}