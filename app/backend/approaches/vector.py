from langchain_core.documents import Document

from backend.approaches.base import ApproachesBase
from backend.approaches.utils import vector_store_api


class Vector(ApproachesBase):
    def run(self, collection_name: str, query: str, limit: int, score_threshold: float) -> tuple[list[Document], str]:
        namespace = f"{self._database_name}.{collection_name}"
        vector_store = vector_store_api(
            namespace=namespace, connection_string=self._connection_string, embedding=self._embedding
        )
        retriever = vector_store.as_retriever(
            search_type="similarity", search_kwargs={"k": limit, "score_threshold": score_threshold}
        )
        vector_response = retriever.invoke(query)
        if vector_response:
            return vector_response, vector_response[0].page_content
        return [], ""
