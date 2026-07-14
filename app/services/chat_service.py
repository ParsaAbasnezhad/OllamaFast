from sqlalchemy.orm import Session

from app.models.chat import Chat
from app.repositories.chat_repository import ChatRepository
from app.repositories.message_repository import MessageRepository
from app.services.ollama_service import OllamaService


class ChatService:

    @staticmethod
    def create_chat(
        db: Session,
        user_id: int,
        title: str
    ) -> Chat:
        return ChatRepository.create(
            db=db,
            user_id=user_id,
            title=title
        )

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

        # خواندن تاریخچه
        history = MessageRepository.get_chat_messages(
            db=db,
            chat_id=chat_id
        )

        # تبدیل به فرمت Ollama
        messages = [
            {
                "role": msg.role,
                "content": msg.content
            }
            for msg in history
        ]

        # ارسال به Ollama
        answer = OllamaService.chat(messages)

        # ذخیره پاسخ AI
        MessageRepository.create(
            db=db,
            chat_id=chat_id,
            role="assistant",
            content=answer
        )

        return {
            "response": answer
        }