from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_answer(question: str, context: str):
    response = client.chat.completions.create(
        model=settings.CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Answer ONLY using the provided context."
                )
            },
            {
                "role": "user",
                "content": f"""
Context:
{context}

Question:
{question}
"""
            }
        ]
    )

    return response.choices[0].message.content