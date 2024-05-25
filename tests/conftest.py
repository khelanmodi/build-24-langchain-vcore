from unittest.mock import AsyncMock, MagicMock, patch

import pytest
import pytest_asyncio
from langchain_core.documents import Document

from quartapp.app import create_app
from quartapp.approaches.base import ApproachesBase
from quartapp.approaches.rag import RAG
from quartapp.approaches.vector import Vector
from quartapp.config import AppConfig


@pytest_asyncio.fixture
async def app():
    app_config = AppConfig()
    app = create_app(app_config=app_config)
    app.config.update(
        {
            "TESTING": True,
        }
    )
    async with app.test_app() as test_app:
        yield test_app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
@patch.object(ApproachesBase, "__abstractmethods__", set())
def approaches_base_mock():
    # Mock quartapp.approaches.base.ApproachesBase
    mock_embedding = MagicMock()

    # Mock Vector Store
    mock_vector_store = MagicMock()
    mock_retriever = MagicMock()
    mock_document = Document(page_content="content")
    mock_retriever.ainvoke = AsyncMock(return_value=[mock_document])
    mock_vector_store.as_retriever.return_value = mock_retriever

    # Mock Chat
    mock_chat = MagicMock()

    return ApproachesBase(mock_vector_store, mock_embedding, mock_chat)  # type: ignore [abstract]


@pytest.fixture
def vector_mock(approaches_base_mock):
    # Mock quartapp.approaches.vector.Vector
    return Vector(approaches_base_mock._vector_store, approaches_base_mock._embedding, approaches_base_mock._chat)


@pytest.fixture
def rag_mock(approaches_base_mock):
    # Mock quartapp.approaches.rag.RAG
    return RAG(approaches_base_mock._vector_store, approaches_base_mock._embedding, approaches_base_mock._chat)
