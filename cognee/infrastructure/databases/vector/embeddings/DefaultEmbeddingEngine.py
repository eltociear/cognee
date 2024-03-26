from typing import List
from fastembed import TextEmbedding
from .EmbeddingEngine import EmbeddingEngine
from cognitive_architecture.config import Config

config = Config()
config.load()
class DefaultEmbeddingEngine(EmbeddingEngine):
    async def embed_text(self, text: List[str]) -> List[float]:
        embedding_model = TextEmbedding(model_name = config.embedding_model)
        embeddings_list = list(map(lambda embedding: embedding.tolist(), embedding_model.embed(text)))

        return embeddings_list

    def get_vector_size(self) -> int:
        return 1024
