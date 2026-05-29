from contextlib import asynccontextmanager
from fastapi import FastAPI
from qdrant_client.models import VectorParams, Distance
from app.services.qdrant_service import client, COLLECTION_NAME


@asynccontextmanager
async def lifespan(app: FastAPI):
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )

    yield