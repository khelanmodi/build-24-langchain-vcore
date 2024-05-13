from typing import Any

from quart import Quart, Response, jsonify, request

from backend.config import AppConfig


def create_app(app_config: AppConfig, test_config=None):
    app = Quart(__name__, template_folder="../frontend", static_folder="../frontend/static")

    if test_config:
        # load the test config if passed in
        app.config.from_mapping(test_config)

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
        retrieval_mode = context.get("overrides", {}).get("retrieval_mode", "vector")
        top = context.get("overrides", {}).get("top", 3)
        score_threshold = context.get("overrides", {}).get("score_threshold", 0.5)
        collection_name = "johncosmoscollection"

        if retrieval_mode == "vector":
            vector_answer = app_config.run_vector(collection_name, messages, top, score_threshold)
            return jsonify({"choices": vector_answer})
        elif retrieval_mode == "rag":
            rag_answer = app_config.run_rag(collection_name, messages, top, score_threshold)
            return jsonify({"choices": rag_answer})
        elif retrieval_mode == "keyword":
            keyword_answer = app_config.run_keyword(collection_name, messages, top, score_threshold)
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
