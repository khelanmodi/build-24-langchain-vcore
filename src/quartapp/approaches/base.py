from abc import ABC, abstractmethod

from langchain_core.documents import Document
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings


class ApproachesBase(ABC):
    def __init__(
        self,
        connection_string: str,
        database_name: str,
        collection_name: str,
        embedding: AzureOpenAIEmbeddings,
        chat: AzureChatOpenAI,
    ):
        self._connection_string = connection_string
        self._database_name = database_name
        self._collection_name = collection_name
        self._embedding = embedding
        self._chat = chat

    @abstractmethod
    def run(self, messages: list, temperature: float, limit: int, score_threshold: float) -> tuple[list[Document], str]:
        raise NotImplementedError
