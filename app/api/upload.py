from fastapi import APIRouter, UploadFile, File
import uuid
from app.services.parser_service import extract_text
from app.utils.chunking import chunk_text
from app.services.embedding_service import create_embedding
from app.services.qdrant_service import client, COLLECTION_NAME

router = APIRouter()


@router.post(
    "/upload",
    summary="Upload document",
    description="Upload a file (PDF, DOCX) for processing."
)
async def upload_document(file: UploadFile = File(...)):
    text = await extract_text(file)

    chunks = chunk_text(text)
    points = []

    for i, chunk in enumerate(chunks):
        vector = create_embedding(chunk)

        points.append({
            "id": str(uuid.uuid4()),
            "vector": vector,
            "payload": {
                "text": chunk,
                "filename": file.filename,
                "chunk_id": i
            }
        })

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    return {
        "filename": file.filename,
        "chunks_uploaded": len(points)
    }