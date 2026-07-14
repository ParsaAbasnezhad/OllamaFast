from sqlalchemy.orm import Session

from app.repositories.message_repository import MessageRepository
from app.services.ollama_service import OllamaService


class MessageService:

    @staticmethod
    def create_message(
        db: Session,
        chat_id: int,
        content: str
    ):
        return MessageRepository.create(
            db=db,
            chat_id=chat_id,
            role="user",
            content=content
        )

    @staticmethod
    def get_chat_messages(
        db: Session,
        chat_id: int
    ):
        return MessageRepository.get_chat_messages(
            db=db,
            chat_id=chat_id
        )

    @staticmethod
    def build_ollama_messages(
        db: Session,
        chat_id: int
    ):
        messages = MessageRepository.get_chat_messages(
            db=db,
            chat_id=chat_id
        )

        return [
            {
                "role": message.role,
                "content": message.content
            }
            for message in messages
        ]

    @staticmethod
    def send_message(
        db: Session,
        chat_id: int,
        content: str
    ):
        # ذخیره پیام کاربر
        MessageRepository.create(
            db=db,
            chat_id=chat_id,
            role="user",
            content=content
        )

        # خواندن تاریخچه گفتگو
        messages = MessageService.build_ollama_messages(
            db=db,
            chat_id=chat_id
        )

        # ارسال به Ollama
        answer = OllamaService.chat(messages)

        # ذخیره پاسخ مدل
        MessageRepository.create(
            db=db,
            chat_id=chat_id,
            role="assistant",
            content=answer
        )

        return answer