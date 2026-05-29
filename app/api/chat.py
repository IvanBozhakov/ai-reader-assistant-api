from fastapi import APIRouter
from app.services.embedding_service import create_embedding
from app.services.qdrant_service import search_similar_chunks
from app.services.openai_service import generate_answer
from app.models.schemas import ChatRequest, ChatResponse

router = APIRouter()

@router.post(
    "/chat",
    response_model=ChatResponse,
    summary="Chat with the assistant",
    description="Send a question and receive an AI-generated answer."
)
async def chat(request: ChatRequest):
    query_vector = create_embedding(request.question)

    chunks = search_similar_chunks(query_vector)

    context = "\n\n".join(chunks)

    answer = generate_answer(
        question=request.question,
        context=context
    )

    return ChatResponse(answer=answer)