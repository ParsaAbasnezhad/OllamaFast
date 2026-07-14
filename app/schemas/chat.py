from pydantic import BaseModel


class ChatCreate(BaseModel):
    user_id: int
    title: str


class ChatResponse(BaseModel):
    id: int
    user_id: int
    title: str

    model_config = {
        "from_attributes": True
    }