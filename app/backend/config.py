import os

from backend.approaches.setup import Setup


class AppConfig:
    def __init__(self):
        openai_embeddings_model = os.getenv("AZURE_OPENAI_EMBEDDINGS_MODEL_NAME", "text-embedding-ada-002")
        openai_embeddings_deployment = os.getenv("AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT_NAME", "text-embedding")
        openai_chat_model = os.getenv("AZURE_OPENAI_CHAT_MODEL_NAME", "gpt-35-turbo")
        openai_chat_deployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME", "chat-gpt")
        connection_string = os.getenv("AZURE_COSMOS_CONNECTION_STRING", "<YOUR-COSMOS-DB-CONNECTION-STRING>")
        database_name = os.getenv("AZURE_COSMOS_DATABASE_NAME", "<COSMOS-DB-NEW-UNIQUE-DATABASE-NAME>")
        api_key = os.getenv("AZURE_OPENAI_API_KEY", "<YOUR-DEPLOYMENT-KEY>")
        api_version = os.getenv("OPENAI_API_VERSION", "2023-09-15-preview")
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "https://<YOUR-OPENAI-DEPLOYMENT-NAME>.openai.azure.com/")
        self.setup = Setup(
            openai_embeddings_model,
            openai_embeddings_deployment,
            openai_chat_model,
            openai_chat_deployment,
            connection_string,
            database_name,
            api_key,
            api_version,
            azure_endpoint,
        )
