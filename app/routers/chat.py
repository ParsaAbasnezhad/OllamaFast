from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from fastapi.responses import StreamingResponse

router = APIRouter()


from app.services.ollama_service import stream_ai


@router.post("/stream")
def stream_chat(request: ChatRequest):
    return StreamingResponse(
        stream_ai(request.message),
        media_type="text/plain",
    )