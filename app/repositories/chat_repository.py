from sqlalchemy.orm import Session

from app.models.chat import Chat


class ChatRepository:

    @staticmethod
    def create(db: Session, user_id: int, title: str) -> Chat:
        chat = Chat(
            user_id=user_id,
            title=title
        )

        db.add(chat)
        db.commit()
        db.refresh(chat)

        return chat