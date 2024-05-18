import pytest
import pytest_asyncio

from quartapp import create_app
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
