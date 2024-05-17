from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain_core.documents import Document

from quartapp.approaches.base import ApproachesBase
from quartapp.approaches.utils import vector_store_api

chat_history_prompt = """Given the following conversation and the last question as a follow up question,
rephrase the follow up question to be a standalone question.

Chat History:
{messages}

Standalone question:"""

context_prompt = """You are a chatbot that can have a conversation about Food dishes from the context.
Answer the following question based only on the provided context:

Context:
{context}

Question: {input}"""


class RAG(ApproachesBase):
    def run(self, messages: list, temperature: float, limit: int, score_threshold: float) -> tuple[list[Document], str]:
        # Create a vector store retriever
        namespace = f"{self._database_name}.{self._collection_name}"
        vector_store = vector_store_api(
            namespace=namespace, connection_string=self._connection_string, embedding=self._embedding
        )
        retriever = vector_store.as_retriever(
            search_type="similarity", search_kwargs={"k": limit, "score_threshold": score_threshold}
        )

        self._chat.temperature = 0.3

        # Create a vector context aware chat retriever
        history_prompt_template = ChatPromptTemplate.from_template(chat_history_prompt)
        history_chain = self._chat | history_prompt_template

        # Rephrase the question
        rephrased_question_prompt = history_chain.invoke(messages)

        rephrased_question = self._chat.invoke(rephrased_question_prompt.to_json()["kwargs"]["messages"][0].content)

        print(rephrased_question.content)
        # Perform vector search
        vector_context = retriever.invoke(rephrased_question.content)

        # Create a vector context aware chat retriever
        context_prompt_template = ChatPromptTemplate.from_template(context_prompt)
        document_chain = create_stuff_documents_chain(self._chat, context_prompt_template)

        self._chat.temperature = temperature

        if vector_context:
            # Perform RAG search
            response = document_chain.invoke({"context": vector_context, "input": rephrased_question.content})

            return vector_context, response

        # Perform RAG search with no context
        response = document_chain.invoke({"context": vector_context, "input": rephrased_question.content})
        return [], response
