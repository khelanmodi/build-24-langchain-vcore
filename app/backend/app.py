from pathlib import Path
from typing import Any

from quart import Quart, Response, jsonify, request, send_file, send_from_directory

from backend.config import AppConfig


def create_app(app_config: AppConfig, test_config=None):
    app = Quart(__name__, static_folder="static")

    if test_config:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    @app.route("/")
    async def index():
        return await send_file(Path(__file__).resolve().parent / "static/index.html")

    @app.route("/favicon.ico")
    async def favicon():
        return await send_file(Path(__file__).resolve().parent / "static/favicon.ico")

    @app.route("/assets/<path:path>")
    async def assets(path):
        return await send_from_directory(Path(__file__).resolve().parent / "static" / "assets", path)

    @app.route("/hello", methods=["GET"])
    async def hello() -> Response:
        return jsonify({"answer": "Hello, World!"})

    @app.route("/chat", methods=["POST"])
    async def chat() -> Any:
        if not request.is_json:
            return jsonify({"error": "request must be json"}), 415
        body = await request.get_json()
        messages = body.get("messages", [])
        context = body.get("context", {})
        override = context.get("overrides", {})
        retrieval_mode = override.get("retrieval_mode", "vector")
        temperature = override.get("temperature", 0.3)
        top = override.get("top", 3)
        score_threshold = override.get("score_threshold", 0.5)
        collection_name = "johncosmoscollection"

        if retrieval_mode == "vector":
            vector_answer = app_config.run_vector(collection_name, messages, temperature, top, score_threshold)
            return jsonify({"choices": vector_answer})
        elif retrieval_mode == "rag":
            rag_answer = app_config.run_rag(collection_name, messages, temperature, top, score_threshold)
            return jsonify({"choices": rag_answer})
        elif retrieval_mode == "keyword":
            keyword_answer = app_config.run_keyword(collection_name, messages, temperature, top, score_threshold)
            return jsonify({"choices": keyword_answer})
        else:
            return jsonify({"error": "Not Implemented!"}), 400

    return app


# Or specify port manually:
"""
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
"""
