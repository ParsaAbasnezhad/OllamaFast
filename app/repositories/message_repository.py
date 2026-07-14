from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.message import Message


class MessageRepository:

    @staticmethod
    def create(
        db: Session,
        chat_id: int,
        role: str,
        content: str
    ) -> Message:

        message = Message(
            chat_id=chat_id,
            role=role,
            content=content
        )

        db.add(message)
        db.commit()
        db.refresh(message)

        return message

    @staticmethod
    def get_chat_messages(db: Session, chat_id: int) -> list[Message]:
        stmt = (
            select(Message)
            .where(Message.chat_id == chat_id)
            .order_by(Message.created_at)
        )

        return db.scalars(stmt).all()