from langchain_core.documents import Document

from backend.approaches.base import ApproachesBase
from backend.approaches.utils import vector_store_api


class Vector(ApproachesBase):
    def run(self, collection_name: str, query: str, limit: int, score_threshold: float) -> list[Document]:
        namespace = f"{self._database_name}.{collection_name}"
        vector_store = vector_store_api(
            namespace=namespace, connection_string=self._connection_string, embedding=self._embedding
        )
        return vector_store.similarity_search(query, k=limit, score_threshold=score_threshold)
