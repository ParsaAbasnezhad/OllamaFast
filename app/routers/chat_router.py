from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.schemas.chat import ChatCreate, ChatResponse
from app.schemas.chat_message import ChatRequest, AIResponse

from app.services.chat_service import ChatService
router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/", response_model=ChatResponse)
def create_chat(
    data: ChatCreate,
    db: Session = Depends(get_db)
):
    return ChatService.create_chat(
        db=db,
        user_id=data.user_id,
        title=data.title
    )

@router.post("/{chat_id}/send", response_model=AIResponse)
def send_message(
    chat_id: int,
    data: ChatRequest,
    db: Session = Depends(get_db)
):
    return ChatService.send_message(
        db=db,
        chat_id=chat_id,
        content=data.content
    )