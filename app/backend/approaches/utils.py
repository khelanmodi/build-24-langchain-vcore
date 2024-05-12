from langchain_community.vectorstores import AzureCosmosDBVectorSearch
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings


def embeddings_api(
    openai_embeddings_model: str, openai_embeddings_deployment: str, api_key: str, api_version: str, azure_endpoint: str
) -> AzureOpenAIEmbeddings:
    return AzureOpenAIEmbeddings(
        model=openai_embeddings_model,
        azure_deployment=openai_embeddings_deployment,
        api_key=api_key,
        api_version=api_version,
        azure_endpoint=azure_endpoint,
    )


def chat_api(
    openai_chat_model: str, openai_chat_deployment: str, api_key: str, api_version: str, azure_endpoint: str
) -> AzureOpenAIEmbeddings:
    return AzureChatOpenAI(
        model=openai_chat_model,
        azure_deployment=openai_chat_deployment,
        api_key=api_key,
        api_version=api_version,
        azure_endpoint=azure_endpoint,
    )


def vector_store_api(
    connection_string: str, namespace: str, embedding: AzureOpenAIEmbeddings
) -> AzureCosmosDBVectorSearch:
    return AzureCosmosDBVectorSearch.from_connection_string(
        connection_string=connection_string,
        namespace=namespace,
        embedding=embedding,
    )