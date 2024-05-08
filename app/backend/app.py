from typing import Any

from quart import Quart, jsonify, request


def create_app(test_config=None):
    app = Quart(__name__, template_folder="../frontend", static_folder="../frontend/static")

    if test_config:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    @app.route("/hello", methods=["GET"])
    async def hello() -> Any:
        return jsonify({"answer": "Hello, World!"})

    @app.route("/chat", methods=["POST"])
    async def chat() -> Any:
        body = await request.get_json()
        return jsonify({"error": "Not Implemented!\nMessage: " + body["messages"][0]["content"]}), 400

    @app.route("/ask", methods=["POST"])
    async def ask() -> Any:
        body = await request.get_json()
        return jsonify({"error": "Not Implemented!\nMessage: " + body["messages"][0]["content"]}), 400

    return app


# Or specify port manually:
"""
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
"""
