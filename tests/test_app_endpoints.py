import pytest
from quart import Response


@pytest.mark.asyncio
async def test_index(client):
    response: Response = await client.get("/")

    html_index_file_path = "src/quartapp/static/index.html"
    with open(html_index_file_path, "rb") as f:
        html_index_file = f.read()

    assert response.status_code == 200
    assert response.content_type == "text/html; charset=utf-8"
    assert response.headers["Content-Length"] == str(len(html_index_file))
    assert html_index_file == await response.data


@pytest.mark.asyncio
async def test_hello(client):
    response: Response = await client.get("/hello")

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.headers["Content-Length"] == "27"
    assert b'{"answer":"Hello, World!"}' in await response.data


@pytest.mark.asyncio
async def test_favicon(client):
    response: Response = await client.get("/favicon.ico")

    favicon_file_path = "src/quartapp/static/favicon.ico"
    with open(favicon_file_path, "rb") as f:
        favicon_file = f.read()

    assert response.status_code == 200
    assert response.content_type == "image/vnd.microsoft.icon"
    assert response.headers["Content-Length"] == str(len(favicon_file))
    assert favicon_file == await response.data


@pytest.mark.asyncio
async def test_assets_non_existent_404(client):
    response: Response = await client.get("/assets/manifest.json")

    assert response.status_code == 404
    assert response.content_type == "application/json"
    assert response.headers["Content-Length"] == "22"
    assert b'{"error":"Not Found"}' in await response.data


@pytest.mark.asyncio
async def test_chat_non_json_415(client):
    response: Response = await client.post("/chat")

    assert response.status_code == 415
    assert response.content_type == "application/json"
    assert response.headers["Content-Length"] == "33"
    assert b'{"error":"request must be json"}' in await response.data
