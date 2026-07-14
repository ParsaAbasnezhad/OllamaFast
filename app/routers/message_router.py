from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database.dependencies import get_db
from app.schemas.message import MessageCreate, MessageResponse
from app.services.message_service import MessageService

router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)


@router.post("/", response_model=MessageResponse)
def create_message(
    data: MessageCreate,
    db: Session = Depends(get_db)
):
    return MessageService.create_message(
        db=db,
        chat_id=data.chat_id,
        content=data.content
    )

@router.get(
    "/{chat_id}",
    response_model=list[MessageResponse]
)
def get_messages(
    chat_id: int,
    db: Session = Depends(get_db)
):
    return MessageService.get_chat_messages(
        db=db,
        chat_id=chat_id
    )