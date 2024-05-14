from abc import ABC

from pydantic.v1 import SecretStr

from backend.approaches.rag import RAG
from backend.approaches.utils import chat_api, embeddings_api
from backend.approaches.vector import Vector


class OpenAISetup(ABC):
    def __init__(
        self,
        openai_embeddings_model: str,
        openai_embeddings_deployment: str,
        openai_chat_model: str,
        openai_chat_deployment: str,
        api_key: SecretStr,
        api_version: str,
        azure_endpoint: str,
    ):
        self._embeddings_api = embeddings_api(
            openai_embeddings_model, openai_embeddings_deployment, api_key, api_version, azure_endpoint
        )
        self._chat_api = chat_api(openai_chat_model, openai_chat_deployment, api_key, api_version, azure_endpoint)


class Setup(ABC):
    def __init__(
        self,
        openai_embeddings_model: str,
        openai_embeddings_deployment: str,
        openai_chat_model: str,
        openai_chat_deployment: str,
        connection_string: str,
        database_name: str,
        api_key: SecretStr,
        api_version: str,
        azure_endpoint: str,
    ):
        self._openai_setup = OpenAISetup(
            openai_embeddings_model,
            openai_embeddings_deployment,
            openai_chat_model,
            openai_chat_deployment,
            api_key,
            api_version,
            azure_endpoint,
        )
        self.vector_search = Vector(
            connection_string=connection_string,
            database_name=database_name,
            embedding=self._openai_setup._embeddings_api,
            chat=self._openai_setup._chat_api,
        )
        self.rag = RAG(
            connection_string=connection_string,
            database_name=database_name,
            embedding=self._openai_setup._embeddings_api,
            chat=self._openai_setup._chat_api,
        )
