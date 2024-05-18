import pytest

from quartapp import create_app
from quartapp.config import AppConfig


def test_config():
    app_config = AppConfig()
    assert not create_app(app_config=app_config).testing
    assert create_app(app_config=app_config, test_config={"TESTING": True}).testing


@pytest.mark.asyncio
async def test_hello(client):
    response = await client.get("/hello")
    data = await response.get_json()

    assert response.status_code == 200
    assert "Hello, World!" in data["answer"]
