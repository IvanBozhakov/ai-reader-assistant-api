from app.config import settings
from qdrant_client import QdrantClient

client = QdrantClient(
    host=settings.QDRANT_HOST,
    port=settings.QDRANT_PORT
)

COLLECTION_NAME = settings.COLLECTION_NAME

def search_similar_chunks(vector, limit: int = 5):
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=vector,
        limit=limit
    )

    return [hit.payload["text"] for hit in results]