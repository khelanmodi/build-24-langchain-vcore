from langchain_core.documents import Document
from langchain_openai import AzureOpenAIEmbeddings


class ApproachesBase:
    def __init__(self, connection_string: str, database_name: str, embedding: AzureOpenAIEmbeddings):
        self._connection_string = connection_string
        self._database_name = database_name
        self._embedding = embedding

    def run(self, namespace: str, query: str) -> list[Document]:
        raise NotImplementedError
