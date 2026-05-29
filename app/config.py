from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OPENAI_API_KEY: str

    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333

    COLLECTION_NAME: str = "documents"

    EMBEDDING_MODEL: str = "text-embedding-3-small"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()