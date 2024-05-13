from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.runnables import Runnable

from backend.approaches.base import ApproachesBase
from backend.approaches.utils import vector_store_api


class RAG(ApproachesBase):
    def run(self, collection_name: str, query: str, limit: int, score_threshold: float) -> tuple[list[Document], str]:
        namespace = f"{self._database_name}.{collection_name}"
        vector_store = vector_store_api(
            namespace=namespace, connection_string=self._connection_string, embedding=self._embedding
        )

        retriever = vector_store.as_retriever(
            search_type="similarity", search_kwargs={"k": limit, "score_threshold": score_threshold}
        )

        prompt = ChatPromptTemplate.from_messages(
            [
                MessagesPlaceholder(variable_name="chat_history"),
                ("user", "{input}"),
                (
                    "user",
                    """Given the above conversation,
                    generate a search query to look up to get information relevant to the conversation""",
                ),
            ]
        )
        retriever_chain = create_history_aware_retriever(self._chat, retriever, prompt)

        prompt_context = ChatPromptTemplate.from_messages(
            [
                ("system", "Answer the user's questions based on the below context:\n\n{context}"),
                MessagesPlaceholder(variable_name="chat_history"),
                ("user", "{input}"),
            ]
        )
        document_chain = create_stuff_documents_chain(llm=self._chat, prompt=prompt_context)

        rag_chain: Runnable = create_retrieval_chain(
            retriever=retriever_chain,
            combine_docs_chain=document_chain,
        )
        response = rag_chain.invoke({"chat_history": [], "input": query})
        return response["context"], response["answer"]
