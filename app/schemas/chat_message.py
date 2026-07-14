from pydantic import BaseModel


class ChatRequest(BaseModel):
    content: str


class AIResponse(BaseModel):
    response: str