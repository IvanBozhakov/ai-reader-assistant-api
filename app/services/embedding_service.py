# from openai import OpenAI
# from app.config import settings
#
# client = OpenAI(api_key=settings.OPENAI_API_KEY)
#
# def create_embedding(text: str):
#     response = client.embeddings.create(
#         model=settings.EMBEDDING_MODEL,
#         input=text
#     )
#
#     return response.data[0].embedding

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embedding(text: str):
    return model.encode(text).tolist()