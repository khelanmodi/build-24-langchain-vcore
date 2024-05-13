from abc import ABC, abstractmethod

from langchain_core.documents import Document
from langchain_openai import AzureOpenAIEmbeddings


class ApproachesBase(ABC):
    def __init__(self, connection_string: str, database_name: str, embedding: AzureOpenAIEmbeddings):
        self._connection_string = connection_string
        self._database_name = database_name
        self._embedding = embedding

    @abstractmethod
    def run(self, collection_name: str, query: str, limit: int, score_threshold: float) -> list[Document]:
        raise NotImplementedError
