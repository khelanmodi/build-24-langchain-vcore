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
        # stream = body.get("stream", False)
        context = body.get("context", {})
        retrieval_mode = context.get("overrides", {}).get("retrieval_mode")
        if retrieval_mode == "vectors":
            collection_name = "johncosmoscollection"
            answer = [
                {
                    "message": {"content": answer.page_content, "role": "system"},
                    "index": answer.metadata.get("seq_num"),
                    "context": {"data_points": [], "thoughts": []},
                    "source": answer.metadata.get("source"),
                }
                for answer in app_config.setup.vector_search.run(collection_name, messages[-1]["content"])
            ]
            return jsonify({"choices": answer})
        return jsonify({"error": "Not Implemented!\nMessage: " + body["messages"][0]["content"]}), 400

    @app.route("/ask", methods=["POST"])
    async def ask() -> Any:
        if not request.is_json:
            return jsonify({"error": "request must be json"}), 415
        body = await request.get_json()
        return jsonify({"error": "Not Implemented!\nMessage: " + body["messages"][0]["content"]}), 400

    return app


# Or specify port manually:
"""
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
"""
